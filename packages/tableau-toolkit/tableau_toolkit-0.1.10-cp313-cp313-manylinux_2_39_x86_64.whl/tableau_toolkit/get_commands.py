import click
from .cli_utils import execute_get_query

from .queries.view_queries import get_views_query
from .queries.workbook_queries import get_workbooks_query
from .queries.datasource_queries import get_datasources_query
from .queries.extract_refresh_queries import get_extract_refreshes_query

from .queries.subscription_queries import get_subscriptions_query
from .queries.data_alert_queries import get_data_alerts_query

from .queries.customized_view_queries import get_customized_views_query
from .queries.user_queries import get_users_query
from .queries.group_queries import get_groups_query


@click.group()
def get():
    """Get various Tableau resources"""


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def customized_views(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get subscriptions with usage data"""
    query = get_customized_views_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def views(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get views with usage data"""
    query = get_views_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def workbooks(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get workbooks with usage data"""
    query = get_workbooks_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option("--luid", default=None, help="Filter by object luid")
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def datasources(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    luid,
    columns,
):
    """Get datasources with usage data"""
    query = get_datasources_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
        "luid": luid,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="content_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def extract_refreshes(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get extract refreshes with usage data"""
    query = get_extract_refreshes_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="content_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def subscriptions(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get subscriptions with usage data"""
    query = get_subscriptions_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--owner-username", default=None, help="Filter by owner username (system_user.name)"
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def data_alerts(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    owner_username,
    columns,
):
    """Get data alerts with usage data"""
    query = get_data_alerts_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "owner_username": owner_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_username", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option("--username", default=None, help="Filter by user name (system_user.name)")
@click.option("--exclude-unlicensed", is_flag=True, help="Exclude unlicensed users")
@click.option(
    "--only-inactive-180d",
    default=False,
    is_flag=True,
    help="Include only users inactive for 180 days",
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def users(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    username,
    exclude_unlicensed,
    only_inactive_180d,
    columns,
):
    """Get users with usage data"""
    query = get_users_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "username": username,
        "exclude_unlicensed": exclude_unlicensed,
        "only_inactive_180d": only_inactive_180d,
    }
    execute_get_query(ctx, query, params, header_map, columns)


@get.command()
@click.option(
    "--header-map",
    default=None,
    help='JSON string to map column names, e.g. \'{"site_name":"Site Name"}\'',
)
@click.option(
    "--headers/--no-headers", default=True, help="Display headers (default: on)"
)
@click.option("--sort-by", default="object_name", help="Column to sort by")
@click.option(
    "--sort-order",
    default="desc",
    type=click.Choice(["asc", "desc"]),
    help="Sort order",
)
@click.option("--limit", default=10, help="Number of results to return")
@click.option(
    "--preview/--no-preview",
    default=False,
    help="Print the query instead of executing it",
)
@click.option("--site-name", default=None, help="Filter by site name")
@click.option(
    "--site-admin-username",
    default=None,
    help="Filter by site admin name (system_user.name)",
)
@click.option(
    "--columns", help="Comma-separated list of columns to return", default=None
)
@click.pass_context
def groups(
    ctx,
    header_map,
    headers,
    sort_by,
    sort_order,
    limit,
    preview,
    site_name,
    site_admin_username,
    columns,
):
    """Get groups with usage data"""
    query = get_groups_query()
    params = {
        "headers": headers,
        "sort_by": sort_by,
        "sort_order": sort_order,
        "limit": limit,
        "preview": preview,
        "site_name": site_name,
        "site_admin_username": site_admin_username,
    }
    execute_get_query(ctx, query, params, header_map, columns)
