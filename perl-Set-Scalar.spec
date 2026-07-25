%define modname	Set-Scalar
%define modver 1.29

Summary:	Basic set operations

Name:		perl-%{modname}
Version:	%{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/daoswald/Set-Scalar
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Set-Scalar-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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






