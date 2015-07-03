#
# Fedora COPR siwinski/libsass spec file for sassc
#
# https://copr.fedoraproject.org/coprs/siwinski/libsass/
# https://github.com/siwinski/libsass-rpms
#
# Copyright (c) 2015 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     sass
%global github_name      sassc
%global github_version   3.2.5
%global github_commit    5d43e94f43f305dd6cc3381463976832b9ef6d98

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

Name:          %{github_name}
Version:       %{github_version}
Release:       1%{?dist}
Summary:       libsass command line driver

Group:         Development/Tools
License:       MIT
URL:           http://libsass.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc >= 4.6
BuildRequires: help2man
BuildRequires: libsass-devel
BuildRequires: libtool
# Tests
%if %{with_tests}
%endif

%description
SassC is a wrapper around libsass [1] used to generate a useful command-line
application that can be installed and packaged for several operating systems.

[1] http://github.com/sass/libsass

**********

Please submit any issues with this RPM at
https://github.com/siwinski/libsass-rpms/issues
and prefix your issue title with "[%name] "


%prep
%setup -qn %{github_name}-%{github_commit}
autoreconf --force --install


%build
%{configure}
make %{?_smp_mflags}

help2man --no-info --version-string=%{version} --output sassc.1 sassc


%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 sassc.1 %{buildroot}%{_mandir}/man1/


%check
%if %{with_tests}
make test
%else
: Tests skipped
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Readme.md
%doc TODO
%doc %{_mandir}/man1/sassc.1*
%{_bindir}/sassc


%changelog
* Thu Jul 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.5-1
- Initial package
