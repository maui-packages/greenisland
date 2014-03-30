# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       greenisland

# >> macros
# << macros

Summary:    The GreenIsland library
Version:    0.2.90
Release:    1
Group:      Applications/System
License:    BSD
Source0:    greenisland-%{version}.tar.bz2
Source100:  greenisland.yaml
Requires:   qt5-plugin-imageformat-jpeg
Requires:   qt5-plugin-imageformat-gif
Requires:   qt5-plugin-imageformat-ico
Requires:   qt5-qtsvg-plugin-imageformat-svg
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Compositor)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  cmake
BuildRequires:  python

%description
GreenIsland is a support library to make QML compositors for Wayland.


%package devel
Summary:    Development files for GreenIsland
Group:      Development/System
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications |
that use the GreenIsland library.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
cd upstream
# << build pre

%cmake .  \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
cd upstream
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libGreenIsland.so.*
%{_libdir}/hawaii/qml/GreenIsland/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/GreenIsland/*
%{_libdir}/cmake/GreenIsland/*
%{_libdir}/libGreenIsland.so
# >> files devel
# << files devel
