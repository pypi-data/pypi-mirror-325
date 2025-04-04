import csv
import sys
import base64
from pathlib import Path
import json
from psycopg import ClientCursor
import yaml
import tableauserverclient as TSC
import psycopg
from psycopg import sql
import click
from psycopg.rows import dict_row

CONFIG_FILE = str(Path.home().joinpath(".tableau_toolkit", "tableau.yaml"))


def get_csv_data(file, stdin, delimiter):
    if stdin:
        return csv.DictReader(sys.stdin, delimiter=delimiter)
    if file:

        def csv_generator(file, delimiter):
            def generate():
                with open(file, "r", encoding="utf-8", newline="") as csv_file:
                    reader = csv.DictReader(csv_file, delimiter=delimiter)
                    yield from reader

            return generate()

        return csv_generator(file, delimiter)
    raise click.UsageError("Either --file or --stdin must be provided")


def get_default_config_path():
    return str(Path.home() / CONFIG_FILE)


def load_config(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def decode_secret(encoded_secret):
    decoded_bytes = base64.b64decode(encoded_secret.split(":")[0])
    return decoded_bytes.decode("utf-8")


def authenticate(config):
    server_url = config["tableau_server"]["url"]
    site_content_url = config["site"]["content_url"]
    api_version = config["api"]["version"]

    if config["authentication"]["type"] == "personal_access_token":
        token_name = config["personal_access_token"]["name"]
        token_secret = decode_secret(config["personal_access_token"]["secret"])
        tableau_auth = TSC.PersonalAccessTokenAuth(
            token_name, token_secret, site_id=site_content_url
        )
    else:
        username = config["tableau_auth"]["username"]
        password = decode_secret(config["tableau_auth"]["password"])
        tableau_auth = TSC.TableauAuth(username, password, site_id=site_content_url)

    server = TSC.Server(server_url, use_server_version=False)
    server.add_http_options({"verify": False})
    server.version = api_version
    server.auth.sign_in(tableau_auth)
    return server


def execute_get_query(ctx, query, params, header_map=None, columns=None):
    config = load_config(ctx.obj["config"])
    params["tableau_server_url"] = config["tableau_server"]["public_url"]
    formatted_query = query.format(
        sort_column=sql.Identifier(params["sort_by"]),
        sort_direction=sql.SQL(params["sort_order"].upper()),
        tableau_server_url=sql.SQL(params["tableau_server_url"]),
    )
    postgres_config = {
        **config["postgres"],
        "password": decode_secret(config["postgres"]["password"]),
    }

    if params["preview"]:
        click.echo("Query to be executed:")
        with psycopg.connect(**postgres_config) as conn:
            with conn.cursor() as cur:
                cur = ClientCursor(conn)
                query_string = cur.mogrify(formatted_query, params)
                click.echo(query_string)
    else:
        with psycopg.connect(**postgres_config) as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(formatted_query, params)

                # Get column names from cursor description
                column_names = [desc[0] for desc in cur.description]
                cur.execute(formatted_query, params)

                if columns:
                    selected_columns = [x.strip() for x in columns.split(",")]
                else:
                    selected_columns = column_names

                # validate selected columns
                invalid_columns = [
                    col for col in selected_columns if col not in column_names
                ]
                if invalid_columns:
                    raise ValueError(f"Invalid columns specified: {invalid_columns}")

                if header_map:
                    mapping = json.loads(header_map)
                    display_headers = [
                        mapping.get(col, col) for col in selected_columns
                    ]
                else:
                    display_headers = selected_columns

                if params["headers"]:
                    click.echo("\t".join(display_headers))

                for row in cur:
                    click.echo(
                        "\t".join(
                            (
                                str(row[col]).replace("\n", "\\n").replace("\t", "\\t")
                                if row[col] is not None
                                else ""
                            )
                            for col in selected_columns
                        )
                    )
