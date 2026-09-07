window.MathJax = {
  loader: { load: ["[tex]/boldsymbol"] },
  tex: {
    packages: { "[+]": ["ams", "configmacros", "boldsymbol"] },
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    macros: {
      real: "{\\mathbb R}", comp: "{\\mathbb C}", field: "{\\boldsymbol F}",
      setv: "{V}", setw: "{W}", setlm: "{\\mathcal L}", matm: "{\\mathcal M}",
      minimize: "{\\operatorname*{minimize}}", maximize: "{\\operatorname*{maximize}}",
      argmin: "{\\operatorname*{argmin}}", argmax: "{\\operatorname*{argmax}}",
      KL: ["{\\newcommand*{\\KL}{KL(#1 \\parallel #2)}}", 2],
      detm: ["{\\newcommand*{\\detm}{\\left\\lvert #1 \\right\\rvert}}", 1],
      roundbr: ["{\\newcommand*{\\roundbr}{\\left( #1 \\right)}}", 1],
      squarebr: ["{\\newcommand*{\\squarebr}{\\left[ #1 \\right]}}", 1],
      diffone: ["{\\newcommand*{\\diffone}{#1^{\\prime}}}", 1],
      difftwo: ["{\\newcommand*{\\difftwo}{#1^{\\prime\\prime}}}", 1],
      diffthree: ["{\\newcommand*{\\diffthree}{#1^{\\prime\\prime\\prime}}}", 1],
    },
  },
  options: { ignoreHtmlClass: ".*|", processHtmlClass: "arithmatex" },
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
