# $Id$
# Authority: dries
# Upstream: Jeff Weisberg <jaw+pause$tcp4me,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chart

Summary: Produce many types of charts
Name: perl-Chart
Version: 2.3
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chart/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.cpan.org/modules/by-module/Chart/Chart-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(GD)

%description
With this module you can produce many types of charts.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README rgb.txt TODO
%dir %{perl_vendorlib}/Chart/
%{perl_vendorlib}/Chart/*

%changelog
* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 2.3-1
- Updated to release 2.3.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
