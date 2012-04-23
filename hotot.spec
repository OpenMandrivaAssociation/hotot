Name:       hotot
Version:    0.9.8
Release:    1
Summary:    Twitter Client 
License:    LGPL
Group:      Networking/Other
URL:        https://hotot.googlecode.com/hg/
Source0:    http://hotot.googlecode.com/files/hotot-0.9.8.tar.gz

BuildRequires:   intltool
BuildRequires:   python-distutils-extra
BuildRequires:   python-devel
Requires:        python-webkitgtk
Requires:        python-notify
Requires:        python-keybinder

%description
Hotot, is a lightweight & open source
Microblogging Client, coding using Python language
and designed for Linux. 

%prep
%setup -q -n shellex-Hotot-c14a972

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
%{_datadir}/apps/desktoptheme/default/icons/*.svg
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
#% {_datadir}/locale/*
%{_datadir}/%{name}/icons/*/apps/hotot.png
%{_datadir}/icons/hicolor/scalable/status/*.svg
