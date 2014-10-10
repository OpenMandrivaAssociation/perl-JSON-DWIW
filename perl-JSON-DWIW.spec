%define upstream_name    JSON-DWIW
%define upstream_version 0.47

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Return a true or false value when
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/JSON/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Other JSON modules require setting several parameters before calling the
conversion methods to do what I want. This module does things by default
that I think should be done when working with JSON in Perl. This module
also encodes and decodes faster than JSON.pm and JSON::Syck in my
benchmarks.

This means that any piece of data in Perl (assuming it's valid unicode)
will get converted to something in JSON instead of throwing an exception.
It also means that output will be strict JSON, while accepted input will be
flexible, without having to set any options.

Encoding
    Perl objects get encoded as their underlying data structure, with the
    exception of Math::BigInt and Math::BigFloat, which will be output as
    numbers, and JSON::DWIW::Boolean, which will get output as a true or
    false value (see the true() and false() methods). For example, a
    blessed hash ref will be represented as an object in JSON, a blessed
    array will be represented as an array. etc. A reference to a scalar is
    dereferenced and represented as the scalar itself. Globs, Code refs,
    etc., get stringified, and undef becomes null.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorarch/JSON
%perl_vendorarch/auto/JSON


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.470.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.470.0-1mdv2011.0
+ Revision: 596613
- update to 0.47

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2011.0
+ Revision: 569939
- update to 0.46

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-2mdv2011.0
+ Revision: 562466
- rebuild
- update to 0.45

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-2mdv2011.0
+ Revision: 555969
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2011.0
+ Revision: 552375
- update to 0.42

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 526450
- update to 0.40

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.1
+ Revision: 461320
- update to 0.39

* Sat Sep 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 444609
- update to 0.38

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2010.0
+ Revision: 443931
- update to 0.37

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 421131
- update to 0.36
- update to 0.36

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-2mdv2010.0
+ Revision: 405951
- force rebuild
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2010.0
+ Revision: 393793
- update to new version 0.35

* Thu Jun 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2010.0
+ Revision: 389095
- update to new version 0.34

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2010.0
+ Revision: 387757
- update to new version 0.33

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.32-2mdv2010.0
+ Revision: 375946
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2010.0
+ Revision: 371686
- import perl-JSON-DWIW


* Mon May 04 2009 cpan2dist 0.32-1mdv
- initial mdv release, generated with cpan2dist

