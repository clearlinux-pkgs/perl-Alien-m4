#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Alien-m4
Version  : 0.21
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-m4-0.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-m4-0.21.tar.gz
Summary  : 'Find or build GNU m4'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Alien-m4-license = %{version}-%{release}
Requires: perl-Alien-m4-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Alien::Build::MM)
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(File::Which)
BuildRequires : perl(File::chdir)
BuildRequires : perl(Importer)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Sub::Info)
BuildRequires : perl(Term::Table)
BuildRequires : perl(Test2::V0)

%description
NAME
Alien::m4 - Find or build GNU m4
VERSION
version 0.21
SYNOPSIS
From a Perl script

%package dev
Summary: dev components for the perl-Alien-m4 package.
Group: Development
Provides: perl-Alien-m4-devel = %{version}-%{release}
Requires: perl-Alien-m4 = %{version}-%{release}

%description dev
dev components for the perl-Alien-m4 package.


%package license
Summary: license components for the perl-Alien-m4 package.
Group: Default

%description license
license components for the perl-Alien-m4 package.


%package perl
Summary: perl components for the perl-Alien-m4 package.
Group: Default
Requires: perl-Alien-m4 = %{version}-%{release}

%description perl
perl components for the perl-Alien-m4 package.


%prep
%setup -q -n Alien-m4-0.21
cd %{_builddir}/Alien-m4-0.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Alien-m4
cp %{_builddir}/Alien-m4-0.21/LICENSE %{buildroot}/usr/share/package-licenses/perl-Alien-m4/f3de9c9b719c6785e72148e6a606dfc96d2d8452
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Alien::m4.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Alien-m4/f3de9c9b719c6785e72148e6a606dfc96d2d8452

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
