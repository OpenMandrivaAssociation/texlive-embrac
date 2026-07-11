%global tl_name embrac
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9a
Release:	%{tl_revision}.1
Summary:	Upright brackets in emphasised text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/embrac
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/embrac.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package redefines the commands \emph and \textit so that parentheses
and square brackets are typeset in an upright font in their arguments.
The package requires expl3 from the l3kernel bundle, and xparse and
l3keys2e from the l3packages bundle.

