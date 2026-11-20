# Conditional build:
%bcond_with	tests	# perform "make test"
#
%define		pdir	Apache
%define		pnam	AuthCookie
Summary:	Apache::AuthCookie - Perl authentication and authorization via cookies
Summary(pl.UTF-8):	Apache::AuthCookie - uwierzytelnianie i autoryzacja w Perlu za pomocą ,,cookie''
Name:		perl-Apache-AuthCookie
Version:	3.32
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/M/MS/MSCHOUT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce1572c7e141e39091d6fdc0fa9950f8
URL:		http://search.cpan.org/dist/Apache-AuthCookie/
BuildRequires:	apache-mod_perl-devel >= 1.24
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.24
Requires:	perl-dirs >= 1.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::AuthCookie allows you to intercept a user's first
unauthenticated access to a protected document. The user will be
presented with a custom form where they can enter authentication
credentials. The credentials are posted to the server where AuthCookie
verifies them and returns a session key.

This version includes Apache2::AuthCookie for mod_perl2.

%description -l pl.UTF-8
Apache::AuthCookie pozwala na przechwycenie pierwszego
nieautoryzowanego zapytania użytkownika o chroniony dokument.
Użytkownik zobaczy formularz, w który będzie musiał wpisać wymagane do
autoryzacji dane. Te dane zostaną wysłane na serwer, gdzie AuthCookie
zweryfikuje je i zwróci identyfikator sesji.

Ta wersja dostarcza również Apache2::AuthCookie dla mod_perl2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo '!' | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# tests require working apache and interactive configuration setting
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mod_perl 1 API, PLD ships only mod_perl 2
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Apache/AuthCookie{,/Params}.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/Apache::AuthCookie{,::Params}.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Apache2/AuthCookie.pm
%{perl_vendorlib}/Apache2/AuthCookie
%{perl_vendorlib}/Apache2_4
%{perl_vendorlib}/Apache/README.apache-2.4.pod
%{perl_vendorlib}/Apache/AuthCookie
%{_mandir}/man3/*
