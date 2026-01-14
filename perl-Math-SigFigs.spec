#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	SigFigs
Summary:	Math::SigFigs - do math with correct handling of significant figures
Summary(pl.UTF-8):	Math::SigFigs - obliczenia z poprawną obsługą cyfr znaczących
Name:		perl-Math-SigFigs
Version:	1.04
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	eb842271073dc19d9168aef0bf72f35f
URL:		http://search.cpan.org/dist/Math-SigFigs/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In many scientific applications, it is often useful to be able to
format numbers with a given number of significant figures, or to do
math in such a way as to maintain the correct number of significant
figures. The rules for significant figures are too complicated to be
handled solely using the sprintf function (unless you happen to be
Randal Schwartz :-).

%description -l pl.UTF-8
W wielu aplikacjach naukowych przydaje się formatowanie liczb z zadaną
liczbą cyfr znaczących albo wykonywanie obliczeń z zachowaniem
poprawnej liczby cyfr znaczących. Zasady dla cyfr znaczących są zbyt
skomplikowane, by mogły być obsłużone przez funkcję sprint (chyba że
ktoś jest Randalem Schwartzem :-)).

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/SigFigs.pm
%{_mandir}/man3/*
