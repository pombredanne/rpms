# $Id: $

# Authority: dries

%define real_version 1.5.2-3

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: OpenRM Scene Graph
Name: openrm
Version: 1.5.2.3
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://www.openrm.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/openrm/openrm-devel-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: i486

BuildRequires: gcc-c++, libjpeg-devel
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}

%description
OpenRM Scene Graph is a developers toolkit that implements a scene graph
API, and which uses OpenGL for hardware accelerated rendering. OpenRM is
intended to be used to construct high performance, portable graphics and
scientific visualization applications on Unix/Linux/Windows platforms. It
supports parallelism at several levels in the application, from use on
distributed memory parallel platforms to single-CPU systems.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n rm152

%{__perl} -pi.orig -e 's|/lib/|/%{_lib}/|g' Makefile
%{__perl} -pi.orig -e 's|-O2 -march=i486|%{optflags}|g' make.cfg

%build
%{__make} %{?_smp_mflags} linux

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/usr
%makeinstall INSTALL_DIR=%{buildroot}/usr
%{__mv} %{buildroot}/usr/docs .

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README FUTUREPLANS LICENSE.html OLD-RELEASENOTES RELEASENOTES VERSION docs
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/rm/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Mon Aug 09 2004 Dries Verachtert <dries@ulyssis.org> - 1.5.2.3-1
- Initial package.
