#ifndef __search_bin_cmd__
#define __search_bin_cmd__
/*****
  command line parser interface -- generated by clig 
  (http://wsd.iitb.fhg.de/~kir/clighome/)

  The command line parser `clig':
  (C) 1995,1997,1998,1999,2000 Harald Kirsch (kir@iitb.fhg.de)
*****/

typedef struct s_Cmdline {
  /***** -ncand: Number of candidates to try to return */
  char ncandP;
  int ncand;
  int ncandC;
  /***** -minfft: Power-of-2 length of the shortest miniFFT */
  char minfftP;
  int minfft;
  int minfftC;
  /***** -maxfft: Power-of-2 length of the longest miniFFT */
  char maxfftP;
  int maxfft;
  int maxfftC;
  /***** -rlo: The low Fourier frequency to check */
  char rloP;
  int rlo;
  int rloC;
  /***** -rhi: The high Fourier frequency to check */
  char rhiP;
  int rhi;
  int rhiC;
  /***** -lobin: The first Fourier frequency in the data file */
  char lobinP;
  int lobin;
  int lobinC;
  /***** -overlap: Fraction of a short FFT length to shift before performing another */
  char overlapP;
  double overlap;
  int overlapC;
  /***** -harmsum: Number of harmonics to sum in the miniFFTs */
  char harmsumP;
  int harmsum;
  int harmsumC;
  /***** -numbetween: Number of points to interpolate per Fourier bin (2 gives the usual bin value and an interbin) */
  char numbetweenP;
  int numbetween;
  int numbetweenC;
  /***** -stack: Number of stacked power spectra making up the data.  (The default means the data are complex amplitudes) */
  char stackP;
  int stack;
  int stackC;
  /***** -interbin: Use interbinning instead of full-blown Fourier interpolation.  (Faster but less accurate and sensitive) */
  char interbinP;
  /***** -noalias: Do not add aliased powers to the harmonic sum.  (Faster but less accurate and sensitive) */
  char noaliasP;
  /***** uninterpreted command line parameters */
  int argc;
  /*@null*/char **argv;
  /***** the whole command line concatenated */
  char *full_cmd_line;
} Cmdline;


extern char *Program;
extern void usage(void);
extern /*@shared*/Cmdline *parseCmdline(int argc, char **argv);

extern void showOptionValues(void);

#endif

