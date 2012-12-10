Name:       hotot
Version:    0.9.8.7
Release:    1
Summary:    Twitter Client 
License:    LGPL
Group:      Networking/Other
URL:        https://hotot.googlecode.com/hg/
Source0:    http://hotot.googlecode.com/files/hotot-%{version}.tar.gz

BuildRequires:   intltool
BuildRequires:   python-distutils-extra
BuildRequires:   python-devel
BuildRequires:   cmake
BuildRequires:   qt4-devel
Requires:        python-webkitgtk
Requires:        python-notify
Requires:        python-keybinder

%description
Hotot, is a lightweight & open source
Microblogging Client, coding using Python language
and designed for Linux. 

%prep
%setup -q -n shellex-Hotot-44272ff

%build
%cmake

%install
pushd build
%makeinstall_std
popd

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}


%files -f %{name}.lang
%{_bindir}/hotot
%{_bindir}/hotot-qt
%{_datadir}/hotot/ext/*
%{_datadir}/applications/%{name}-qt.desktop
#% {_datadir}/apps/desktoptheme/default/icons/*.svg
%{_datadir}/hotot/sound/*.wav
%{_datadir}/%{name}/_locales/*/*
%{_datadir}/%{name}/js/*
%{_datadir}/%{name}/css/*
%{_datadir}/%{name}/theme/*
%{_datadir}/%{name}/image/*
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.json
%{_datadir}/applications/hotot.desktop
%{python_sitearch}/*
%{_iconsdir}/hicolor/*/apps/*.*
%{_datadir}/%{name}/icons/*/apps/hotot.png
%{_datadir}/icons/hicolor/scalable/status/*.svg


%changelog
* Tue Jun 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.8.7-1
+ Revision: 802697
- hotot_qt4 removed
- version update 0.9.8.7

* Thu Apr 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.8-1
+ Revision: 793502
- file not found fix
- BR:cmake qt4
- version update 0.9.8

* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.9.5-2mdv2011.0
+ Revision: 597002
- new version 0.9.5
- changed it to use upstream archives
- new build require: 7z

* Tue Oct 12 2010 Juan Luis Baptiste <juancho@mandriva.org> 0.9.4-2mdv2011.0
+ Revision: 585253
- Added missing python-devel BuildRequires.
- Fixed license
- Fixed some rpmlint warnings and some style issues.

  + Gonzalo Igartua <legion@mandriva.org>
    - Modified setup python setup.py install adding --install-lib
    - Modified setup python setup.py install adding --install-lib
    - import hotot

