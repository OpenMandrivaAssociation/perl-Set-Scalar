%define module  Set-Scalar
%define name	perl-%{module}
%define version 1.20
%define release %mkrel 3

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Basic set operations
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}/
Source:		    http://www.cpan.org/modules/by-module/Tree/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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

