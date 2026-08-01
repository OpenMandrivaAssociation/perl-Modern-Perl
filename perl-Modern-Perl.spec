%define upstream_name    Modern-Perl
%define upstream_version 1.20250607
Name:       perl-%{upstream_name}
Version:1.20250607
Release:49

Summary:    Enable all of the features of Modern Perl with one command
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/chromatic/Modern-Perl
Source0:https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20250607.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch: noarch

%description
Enable all of the features of Modern Perl with one command.

%prep
%setup -q -n Modern-Perl-1.20250607

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test || :

%install
%make_install

%files
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*
