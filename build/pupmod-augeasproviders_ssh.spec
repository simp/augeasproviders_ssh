%define mod_name augeasproviders_ssh

Summary: SSH Augeas-based providers for Puppet
Name: pupmod-augeasproviders_ssh
Version: 2.5.0
Release: 0
License: Apache License, 2.0
Group: Applications/System
URL: https://github.com/hercules-team/%{mod_name}
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Requires: pupmod-augeasproviders_core >= 2.0.1
Requires: simp-bootstrap >= 4.2.0
Requires: puppet

Prefix: /etc/puppet/environments/simp/modules

%description
This module provides types/providers for ssh configuration files using the Augeas configuration API library.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/%{mod_name}

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/%{mod_name}
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/%{mod_name}

%files
%defattr(0640,root,puppet,0750)
%{prefix}/%{mod_name}

%post
#!/bin/sh

%postun
# Post uninstall stuff

%changelog
* Sat Aug 01 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.5.0-0
- Updated to the latest %{mod_name}
- Reverted all of the patches that we needed to make since they appear to have
  fixed the issues that we found.

* Wed Feb 18 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.1-0
- First release of %{mod_name} from Team Hercules
