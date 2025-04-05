from kabaret import flow
from kabaret.flow.object import _Manager
from libreflow.baseflow.file import (
    TrackedFile,
    History,
    Revisions,
    Revision,
    PublishFileAction,
    PublishFileFromWorkingCopy
)


class LigneRevisions(Revisions):

    # Modify revision padding to two digits

    def add(self, name=None, is_working_copy=False, comment="", ready_for_sync=True, path_format=None, from_revision=None, init_status=None):
        if not name:
            publication_count = len([r for r in self.mapped_items() if not r.is_working_copy()])
            name = 'v%02i' % (publication_count + 1)
        
        if not is_working_copy:
            init_status = init_status or 'init'

        r = super(Revisions, self).add(name)
        r.configure(
            creator_name=self.root().project().get_user_name(),
            is_working_copy=is_working_copy,
            site_name=self.root().project().admin.multisites.current_site_name.get(),
            status='Available',
            comment=comment,
            ready_for_sync=ready_for_sync,
            from_revision=from_revision,
            init_status=init_status
        )
        r.update_status()
        r.update_path(path_format)

        self._document_cache = None # Reset map cache
        
        return r


def publish(parent):
    if isinstance(parent, History):
        r = flow.Child(LigneRevisions)
        r.name = 'revisions'
        return r


def install_extensions(session):
    return {
        "ligne": [
            publish,
        ]
    }


from . import _version
__version__ = _version.get_versions()['version']
