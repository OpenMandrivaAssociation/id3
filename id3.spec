%define name id3
%define version 0.78
%define release 7

Summary: Command line ID3 tagger
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://home.wanadoo.nl/squell/files/%{name}-%{version}.tar.bz2
Patch: id3-0.78-missing-headers.patch
License: BSD
Group: Sound
Url: http://home.wanadoo.nl/squell/id3.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
id3 mass tagger is a tool for manipulating id3 and id3v2 tags in
multiple files. It can generate tag fields from the filename and
other variables, and/or rename files, using an intuitive syntax. id3
currently supports the old-style ID3 tags (ID3 v1.1), Lyrics3 tags
(Lyrics3 v2.0), and the more complicated ID3v2 (ID3 v2.2.0, v2.3.0)
format. This also means use is pretty much limited to audio files
which use these formats, e.g, MPEG-1 Layer III.

%prep
%setup -q
%patch -p1

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 -D id3 %buildroot%_bindir/id3
install -m 644 -D id3.man %buildroot%_mandir/man1/id3.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES COPYING
%_bindir/id3
%_mandir/man1/id3.1*


%changelog
* Wed Dec 07 2011 Götz Waschk <waschk@mandriva.org> 0.78-5mdv2012.0
+ Revision: 738500
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.78-4mdv2011.0
+ Revision: 611172
- rebuild

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.78-3mdv2010.1
+ Revision: 437933
- rebuild

* Thu Mar 12 2009 Götz Waschk <waschk@mandriva.org> 0.78-2mdv2009.1
+ Revision: 354150
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.78-1mdv2008.1
+ Revision: 140756
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Götz Waschk <waschk@mandriva.org> 0.78-1mdv2008.0
+ Revision: 73344
- Import id3



* Mon Aug 28 2006 Götz Waschk <waschk@mandriva.org> 0.78-1mdv2007.0
- initial package
