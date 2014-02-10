%define modname	Set-Scalar
%define modver 1.27

Summary:	Basic set operations
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Set/Set-Scalar-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Basic set operations.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Set
%{_mandir}/man3/*



