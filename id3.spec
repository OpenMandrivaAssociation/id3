%define name id3
%define version 0.78
%define release %mkrel 3

Summary: Command line ID3 tagger
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://home.wanadoo.nl/squell/files/%{name}-%{version}.tar.bz2
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
