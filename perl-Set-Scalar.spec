%define module  Set-Scalar
%define name	perl-%{module}
%define version 1.22
%define release %mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Basic set operations
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Set/%{module}-%{version}.tar.gz
BuildArch:	    noarch

%description
Basic set operations.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Set
%{_mandir}/*/*

