%define upstream_name    Set-Scalar
%define upstream_version 1.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Basic set operations
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Basic set operations.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-4mdv2012.0
+ Revision: 765641
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-3
+ Revision: 764153
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.250.0-2
+ Revision: 676774
- rebuild

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2011.0
+ Revision: 483044
- update to 1.25

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 404387
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2010.0
+ Revision: 383540
- update to new version 1.24

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.1
+ Revision: 331148
- update to new version 1.23
- update to new version 1.23

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.22-4mdv2009.0
+ Revision: 258355
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.22-3mdv2009.0
+ Revision: 246414
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.1
+ Revision: 104471
- new version

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-3mdv2008.0
+ Revision: 86843
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-2mdv2007.0
- spec cleanup
- fix directory ownership
- better summary and description
- %%mkrel

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdk
- New release 1.20

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.19-1mdk
- initial Mandriva package

