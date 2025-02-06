import cerulean
import pytest

from cerulean import make_file_system, make_terminal, make_scheduler


def test_make_file_system() -> None:
    with make_file_system('local') as fs1:
        assert isinstance(fs1, cerulean.LocalFileSystem)

    cred = cerulean.PasswordCredential('cerulean', 'kingfisher')
    with make_file_system('sftp', 'cerulean-test-ssh', cred) as fs2:
        assert isinstance(fs2, cerulean.SftpFileSystem)

    with make_file_system('sftp', 'cerulean-test-ssh:22', cred) as fs3:
        assert isinstance(fs3, cerulean.SftpFileSystem)

    with make_file_system('webdav', 'http://cerulean-test-webdav/files') as fs4:
        assert isinstance(fs4, cerulean.WebdavFileSystem)

    with pytest.raises(ValueError):
        make_file_system('sftp')

    with pytest.raises(ValueError):
        make_file_system('non-existent-protocol')


def test_make_terminal() -> None:
    with make_terminal('local') as t1:
        assert isinstance(t1, cerulean.LocalTerminal)

    cred = cerulean.PasswordCredential('cerulean', 'kingfisher')
    with make_terminal('ssh', 'cerulean-test-ssh', cred) as t2:
        assert isinstance(t2, cerulean.SshTerminal)

    with make_terminal('ssh', 'cerulean-test-ssh:22', cred) as t3:
        assert isinstance(t3, cerulean.SshTerminal)

    with pytest.raises(ValueError):
        make_terminal('ssh')

    with pytest.raises(ValueError):
        make_terminal('non-existent-protocol')


def test_make_scheduler() -> None:
    with make_terminal('local') as term:
        s1 = make_scheduler('directgnu', term)
        assert isinstance(s1, cerulean.DirectGnuScheduler)

    cred = cerulean.PasswordCredential('cerulean', 'kingfisher')
    with make_terminal('ssh', 'cerulean-test-slurm-17-11', cred) as term2:
        s2 = make_scheduler('directgnu', term2)
        assert isinstance(s2, cerulean.DirectGnuScheduler)

        s3 = make_scheduler('slurm', term2)
        assert isinstance(s3, cerulean.SlurmScheduler)

        with pytest.raises(ValueError):
            make_scheduler('non-existent-scheduler', term2)

    with make_terminal('ssh', 'cerulean-test-torque-6', cred) as term3:
        s4 = make_scheduler('torque', term3)
        assert isinstance(s4, cerulean.TorqueScheduler)

    with make_terminal('ssh', 'cerulean-test-slurm-18-08', cred) as term4:
        s5 = make_scheduler('slurm', term4, 'CERULEAN_TEST=3 ')
        assert isinstance(s5, cerulean.SlurmScheduler)
        assert s5._SlurmScheduler__prefix == 'CERULEAN_TEST=3 '  # type: ignore
