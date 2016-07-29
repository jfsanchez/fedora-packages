%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:            google-docs-fs
Version:         1.0rc1
Release:         1%{?dist}
Summary:         A file system to access Google Docs using any computer

Group:           Applications/Internet
License:         GPLv2
URL:             http://code.google.com/p/google-docs-fs
Source0:         http://google-docs-fs.googlecode.com/files/google-docs-fs-%{version}.tar.gz

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   python >= 2.5, fuse, fuse-python, python-gdata
Requires:        fuse-python, python-gdata

%description
Fuse file system for the google docs service.

A file system to access Google Docs using any computer.

This project aims to allow you to connect to Google Docs and treat it as a 
file system. Combine the portability of Google Docs with the flexibility and 
power of using the office suite of your choice.

This will allow you to mount your Google Docs account as you would a normal 
file system. You will then be able to use it as if it were a file system on your
hard disk, with all operations being transmitted seamlessly to Google Docs.

Written in Python using the FUSE API. This project is handy for Ubuntu 
packaging, the real code is hosted on google code.

 https://launchpad.net/google-docs-fs

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/gmount
%{_bindir}/gmount.py
%{_bindir}/gumount
%{python_sitelib}/google_docs_fs-%{version}-py*.egg-info
%{python_sitelib}/googledocsfs/__init__*
%attr(0755, root, root) %{python_sitelib}/googledocsfs/g*
%doc README.txt LICENSE.txt

%changelog
* Sun Apr 29 2012 Jose Sanchez <jose@serhost.com> - 1.0rc1-1
- Packaged google-docs-fs 4ecdb3d2f8a4 by Scott C. Walton <d38dm8nw81k1ng@gmail.com>
- Download the latest version using mercurial:
- hg clone https://google-docs-fs.googlecode.com/hg/ google-docs-fs
