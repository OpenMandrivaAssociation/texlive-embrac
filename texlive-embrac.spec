Name:		texlive-embrac
Version:	57814
Release:	2
Summary:	Upright brackets in emphasised text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/embrac
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines the commands \emph and \textit so that
parentheses and square brackets are typeset in an upright font
in their arguments. The package requires expl3 from the
l3kernel bundle, and xparse and l3keys2e from the l3packages
bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/embrac/embrac.sty
%doc %{_texmfdistdir}/doc/latex/embrac/README
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_en.pdf
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_en.tex
%doc %{_texmfdistdir}/doc/latex/embrac/embrac_kerning_test.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
