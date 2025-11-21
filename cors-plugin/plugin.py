from tutor import hooks


hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-lms-common-settings",
        """
CORS_ORIGIN_WHITELIST = list(CORS_ORIGIN_WHITELIST) + [
    'null',
]
        """.strip(),
    ),
)

hooks.Filters.ENV_PATCHES.add_item(
    (
        "openedx-cms-common-settings",
        """
CORS_ORIGIN_WHITELIST = list(CORS_ORIGIN_WHITELIST) + [
    'null',
]
        """.strip(),
    ),
)