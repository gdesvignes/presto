#ifndef __search_rzw_cmd__
#define __search_rzw_cmd__
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
  /***** -zlo: The low Fourier frequency to check */
  char zloP;
  int zlo;
  int zloC;
  /***** -zhi: The high Fourier frequency to check */
  char zhiP;
  int zhi;
  int zhiC;
  /***** -rlo: The lowest Fourier frequency to check */
  char rloP;
  int rlo;
  int rloC;
  /***** -rhi: The highest Fourier frequency to check */
  char rhiP;
  int rhi;
  int rhiC;
  /***** -lobin: The first Fourier frequency in the data file */
  char lobinP;
  int lobin;
  int lobinC;
  /***** -zapfile: A file containing a list of freqs to ignore (i.e. RFI) */
  char zapfileP;
  char* zapfile;
  int zapfileC;
  /***** -baryv: The earth's radial velocity component (v/c) towards the observation (used to convert topocentric birdie freqs to barycentric) */
  char baryvP;
  double baryv;
  int baryvC;
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

