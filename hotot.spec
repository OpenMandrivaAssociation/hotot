Name:       hotot
Version:    0.9.5
Release:    %mkrel 2
Summary:    Twitter Client 
License:    LGPL
Group:      Networking/Other
URL:        https://hotot.googlecode.com/hg/
Source0:    http://hotot.googlecode.com/files/hotot-0.9.5_hg~20101108.531.7z
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:	 p7zip
BuildRequires:   intltool
BuildRequires:   python-distutils-extra
BuildRequires:   python-devel
Requires:        python-webkitgtk
Requires:        python-notify
Requires:        python-keybinder

%description
Hotot, is a lightweight & open source Microblogging Client, coding using Python language
and designed for Linux. 

%prep
rm -rf hotot/
7z x %SOURCE0

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
cd hotot/
python setup.py install --root=%{buildroot}\
                        --prefix=%{_prefix}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root,-)

%{_bindir}/hotot
%{python_sitelib}/*
%{_datadir}/hotot/ext/*
%{_datadir}/hotot/ui/*
%{_datadir}/hotot/sound/*.wav
%{_datadir}/locale/*
%{_datadir}/applications/hotot.desktop
%{_datadir}/pixmaps/hotot.png
