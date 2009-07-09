%define realname   JSON-DWIW
%define version    0.35
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Return a true or false value when
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/JSON/%{realname}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{realname}-%{version} 

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

