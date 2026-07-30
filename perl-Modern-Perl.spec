%define upstream_name    Modern-Perl
%define upstream_version 1.20250607
Name:       perl-%{upstream_name}
Version:	1.20250607
Release:	1

Summary:    Enable all of the features of Modern Perl with one command
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/chromatic/Modern-Perl
Source0:	https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-1.20250607.tar.gz

BuildRequires: perl(Test::Simple)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




