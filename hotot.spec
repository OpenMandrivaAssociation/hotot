#
# SPEC file for hotot
#

%define name hotot
%define version 0.9.4
%define release %mkrel 1

Name:%{name}
Version:%{version}
Release:%{release}
Summary:Twitter Client 
License:GNU GLP
Group:Applications/Internet
URL:https://hotot.googlecode.com/hg/
Source:hotot-%{version}.tar.bz2
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}


BuildRequires:intltool
BuildRequires:python-distutils-extra
Requires:python-webkitgtk
Requires:python-notify
Requires:python-keybinder

%description
Hotot, is a lightweight & open source Microblogging Client, coding using Python language
and designed for Linux. 

%prep

%setup -qn hotot

cd hotot/

%build

%install

rm -rf $RPM_BUILD_ROOT

python setup.py install --prefix=${RPM_BUILD_ROOT}/usr

%post

%{update_menus}

%postun

%{clean_menus}

%files
%defattr(-,root,root,-)

%{_bindir}/hotot
%{_libdir}/python2.6/site-packages/hotot-1.0-py2.6.egg-info
%{_libdir}/python2.6/site-packages/hotot/*
%{_datadir}/hotot/ext/*
%{_datadir}/hotot/ui/*
%{_datadir}/locale/es_MX/LC_MESSAGES/hotot.mo
%{_datadir}/locale/pt_PT/LC_MESSAGES/hotot.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/hotot.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/hotot.mo
%{_datadir}/applications/hotot.desktop
%{_datadir}/pixmaps/hotot.png


%clean
rm -rf $RPM_BUILD_ROOT

