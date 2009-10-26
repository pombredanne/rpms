# $Id$
# Authority: dries
# Upstream: Jeff Lavallee <jeff$zeroclue,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

### BEGIN KLUDGE
## temporary fix until package builders install rpm-macros-rpmforge in their
## build environments; once that's done, remove the kludge
## 2009-10-26 shuff

# prevent anything matching from being scanned for provides
%define filter_provides_in(P) %{expand: \
%global __filter_prov_cmd %{?__filter_prov_cmd} %{__grep} -v %{-P} '%*' | \
}

# prevent anything matching from being scanned for requires
%define filter_requires_in(P) %{expand: \
%global __filter_req_cmd %{?__filter_req_cmd} %{__grep} -v %{-P} '%*' | \
}

# filter anything matching out of the provides stream
%define filter_from_provides() %{expand: \
%global __filter_from_prov %{?__filter_from_prov} | %{__sed} -e '%*' \
}

# filter anything matching out of the requires stream
%define filter_from_requires() %{expand: \
%global __filter_from_req %{?__filter_from_req} | %{__sed} -e '%*' \
}

# actually set up the filtering bits 
%define filter_setup %{expand: \
%global _use_internal_dependency_generator 0 \
%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u \
%global __find_provides /bin/sh -c "%{?__filter_prov_cmd} %{__deploop P} %{?__filter_from_prov}" \
%global __find_requires /bin/sh -c "%{?__filter_req_cmd}  %{__deploop R} %{?__filter_from_req}" \
}
### END KLUDGE

%define real_name Yahoo-Marketing

Summary: Interface for Yahoo! Search Marketing's Web Services
Name: perl-Yahoo-Marketing
Version: 6.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-Marketing/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-Marketing-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Cache::Cache) >= 1.01
BuildRequires: perl(Class::Accessor::Chained) >= 0.01
BuildRequires: perl(Crypt::SSLeay) >= 0.40
BuildRequires: perl(DateTime::Format::ISO8601)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(Error) >= 0.15
BuildRequires: perl(Module::Build) >= 0.26
BuildRequires: perl(SOAP::Lite) >= 0.66
# BuildRequires: perl(Scalar::Util) >= 1.01 conflicts with perl package
BuildRequires: perl(Test::Class) >= 0.10
#BuildRequires: perl(Test::More) conflicts with perl package
#BuildRequires: perl(Test::Simple) >= 0.60  conflicts with perl package
BuildRequires: perl(XML::XPath) >= 1.10
BuildRequires: perl(YAML) >= 0.01
BuildRequires: perl >= 5.6.1
Requires: perl(Cache::Cache) >= 1.01
Requires: perl(Class::Accessor::Chained) >= 0.01
Requires: perl(Crypt::SSLeay) >= 0.40
Requires: perl(DateTime::Format::ISO8601)
Requires: perl(DateTime::Format::W3CDTF)
Requires: perl(Error) >= 0.15
Requires: perl(Module::Build) >= 0.26
Requires: perl(SOAP::Lite) >= 0.66
#Requires: perl(Scalar::Util) >= 1.01 conflicts with perl package
Requires: perl(Test::Class) >= 0.10
#Requires: perl(Test::More) conflicts with perl package
#Requires: perl(Test::Simple) >= 0.60 conflicts with perl package
Requires: perl(XML::XPath) >= 1.10
Requires: perl(YAML) >= 0.01
Requires: perl >= 5.6.1

%filter_from_requires /^perl*/d
%filter_setup

%description
An interface for Yahoo! Search Marketing's Web Services.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Yahoo::Marketing.3pm*
%doc %{_mandir}/man3/Yahoo::Marketing::*.3pm*
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/Marketing/
%{perl_vendorlib}/Yahoo/Marketing.pm

%changelog
* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 6.02-1
- Updated to version 6.02.

* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 5.21-1
- Updated to version 5.21.

* Tue Jul 28 2009 Christoph Maser <cmr@financial.com> - 5.10-1
- Updated to version 5.10.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 5.06-1
- Updated to version 5.06.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 4.04-1
- Updated to release 4.04.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 4.03-1
- Updated to release 4.03.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 4.02-1
- Updated to release 4.02.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 3.02-1
- Updated to release 3.02.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 3.01-1
- Updated to release 3.01.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
