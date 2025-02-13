// SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2003-24 Bradley M. Bell
// ----------------------------------------------------------------------------
/*
{xrst_begin adolc_ode.cpp}

Adolc Speed: Ode
################

Specifications
**************
See :ref:`link_ode-name` .

Implementation
**************

{xrst_spell_off}
{xrst_code cpp} */
// suppress conversion warnings before other includes
# include <cppad/wno_conversion.hpp>
//
# include <adolc/adolc.h>

# include <cppad/utility/vector.hpp>
# include <cppad/speed/ode_evaluate.hpp>
# include <cppad/speed/uniform_01.hpp>

// list of possible options
# include <map>
extern std::map<std::string, bool> global_option;

bool link_ode(
   size_t                     size       ,
   size_t                     repeat     ,
   CppAD::vector<double>      &x         ,
   CppAD::vector<double>      &jac
)
{
   // speed test global option values
   if( global_option["atomic"] )
      return false;
   if( global_option["memory"] || global_option["optimize"] )
      return false;
   // -------------------------------------------------------------
   // setup
   assert( x.size() == size );
   assert( jac.size() == size * size );

   typedef CppAD::vector<adouble> ADVector;
   typedef CppAD::vector<double>  DblVector;

   size_t i, j;
   short  tag    = 0;       // tape identifier
   int    keep   = 0;       // do not keep forward mode results
   size_t p      = 0;       // use ode to calculate function values
   size_t n      = size;    // number of independent variables
   size_t m      = n;       // number of dependent variables
   ADVector  X(n), Y(m); // independent and dependent variables
   DblVector f(m);       // function value

   // set up for thread_alloc memory allocator (fast and checks for leaks)
   using CppAD::thread_alloc; // the allocator
   size_t size_min;           // requested number of elements
   size_t size_out;           // capacity of an allocation

   // raw memory for use with adolc
   size_min = size_t(n);
   double *x_raw   = thread_alloc::create_array<double>(size_min, size_out);
   size_min = size_t(m * n);
   double *jac_raw = thread_alloc::create_array<double>(size_min, size_out);
   size_min = size_t(m);
   double **jac_ptr = thread_alloc::create_array<double*>(size_min, size_out);
   for(i = 0; i < m; i++)
      jac_ptr[i] = jac_raw + i * n;

   // -------------------------------------------------------------
   if( ! global_option["onetape"] ) while(repeat--)
   {  // choose next x value
      uniform_01( size_t(n), x);

      // declare independent variables
      trace_on(tag, keep);
      for(j = 0; j < n; j++)
         X[j] <<= x[j];

      // evaluate function
      CppAD::ode_evaluate(X, p, Y);

      // create function object f : X -> Y
      for(i = 0; i < m; i++)
         Y[i] >>= f[i];
      trace_off();

      // evaluate the Jacobian
      for(j = 0; j < n; j++)
         x_raw[j] = x[j];
      jacobian(tag, int(m), int(n), x_raw, jac_ptr);
   }
   else
   {  // choose next x value
      uniform_01( size_t(n), x);

      // declare independent variables
      trace_on(tag, keep);
      for(j = 0; j < n; j++)
         X[j] <<= x[j];

      // evaluate function
      CppAD::ode_evaluate(X, p, Y);

      // create function object f : X -> Y
      for(i = 0; i < m; i++)
         Y[i] >>= f[i];
      trace_off();

      while(repeat--)
      {  // get next argument value
         uniform_01( size_t(n), x);
         for(j = 0; j < n; j++)
            x_raw[j] = x[j];

         // evaluate jacobian
         jacobian(tag, int(m), int(n), x_raw, jac_ptr);
      }
   }
   // convert return value to a simple vector
   for(i = 0; i < m; i++)
   {  for(j = 0; j < n; j++)
         jac[i * n + j] = jac_ptr[i][j];
   }
   // ----------------------------------------------------------------------
   // tear down
   thread_alloc::delete_array(x_raw);
   thread_alloc::delete_array(jac_raw);
   thread_alloc::delete_array(jac_ptr);

   return true;
}
/* {xrst_code}
{xrst_spell_on}

{xrst_end adolc_ode.cpp}
*/
