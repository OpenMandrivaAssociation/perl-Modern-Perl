%define upstream_name    Modern-Perl
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Enable all of the features of Modern Perl with one command
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Modern/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Simple)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 655048
- rebuild for updated spec-helper

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 530458
- import perl-Modern-Perl


* Wed Mar 31 2010 cpan2dist 1.03-1mdv
- initial mdv release, generated with cpan2dist
