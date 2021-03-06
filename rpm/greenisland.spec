# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       greenisland

# >> macros
# << macros

Summary:    The GreenIsland library
Version:    0.5.90+git0
Release:    1
Group:      System/Libraries
License:    GPLv2+, LGPLv2.1+
URL:        https://github.com/mauios/greenisland.git
Source0:    %{name}-%{version}.tar.xz
Source100:  greenisland.yaml
Requires:   qt5-plugin-imageformat-jpeg
Requires:   qt5-plugin-imageformat-gif
Requires:   qt5-plugin-imageformat-ico
Requires:   qt5-qtsvg-plugin-imageformat-svg
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires:   xkeyboard-config
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Compositor)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  ki18n-devel
BuildRequires:  kservice-devel
BuildRequires:  plasma-devel
BuildRequires:  kpackage-devel
BuildRequires:  libkscreen-devel

%description
GreenIsland is a support library to make QML compositors for Wayland.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
export PATH=%{_qt5_bindir}:$PATH
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE.LGPL README.md
%{_bindir}/*
%{_prefix}/%{_lib}/qt5/qml/GreenIsland/*
%{_kf5_plugindir}/*
# >> files
# << files
