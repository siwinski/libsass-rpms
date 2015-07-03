#
# Fedora COPR siwinski/libsass spec file for libsass
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
%global github_name      libsass
%global github_version   3.2.5
%global github_commit    0e6b4a2850092356aa3ece07c6b249f0221caced

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

Name:          libsass
Version:       %{github_version}
Release:       1%{?dist}
Summary:       A C/C++ implementation of a Sass compiler

Group:         Development/Libraries
License:       MIT
URL:           http://libsass.org/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc >= 4.6
BuildRequires: libtool
# Tests
%if %{with_tests}
%endif

%description
Sass [1] is a pre-processing language for CSS. It allows you to write cleaner
stylesheets and makes collaboration on your CSS a breeze. There's a ton of
information on Sass out there, so we won't repeat it all here. Just make sure
to check out the Sass site [2] for tutorials and examples.

Sass was originally written in Ruby. Ruby's great, but people started having a
couple of issues. First, we want everyone to enjoy Sass, no matter what language
they use. Why restrict everyone to using Ruby? In addition, Ruby can be kind of
slow. Lowering compile time for users is important. Enter LibSass.

LibSass is a C/C++ port of the Sass engine. The point is to be simple, fast, and
easy to integrate. Find out more about the project over at Github [3].

[1][2] http://sass-lang.com/
[3] https://github.com/%{github_owner}/%{github_name}

**********

Please submit any issues with this RPM at
https://github.com/siwinski/libsass-rpms/issues
and prefix your issue title with "[%name] "


%package     devel
Summary:     Development files for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%setup -qn %{github_name}-%{github_commit}
autoreconf --force --install


%build
%{configure} --disable-static --enable-shared
make %{?_smp_mflags}


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%check
%if %{with_tests}
make test
%else
: Tests skipped
%endif


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc Readme.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jul 02 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 3.2.5-1
- Initial package
