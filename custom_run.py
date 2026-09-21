import argparse

from confluence_migration_corrected import ConfluenceToAzureDevOpsHierarchicalMigrator


# Configure your settings
confluence_config = {
    'base_url': 'https://xxx.atlassian.net',
    'username': 'xx@hotmail.com',
    'api_token': '',
    'space_key': '~5fff40043d3dea'
}

azuredevops_config = {
    'organization': 'xxxx',
    'project': 'POC-Migration',
    'wiki_identifier': 'POC-Migration.wiki',
    'personal_access_token': ''
}

mapconfig ={
    'users_file': 'users.txt',
    'items_journal_file': 'itemsJournal.txt'
}

# Run migration
migrator = ConfluenceToAzureDevOpsHierarchicalMigrator(
    confluence_config, azuredevops_config,
    users_file=mapconfig['users_file'], items_journal_file=mapconfig['items_journal_file']
)

success = migrator.migrate_space_corrected('~5fff40043d3dea')