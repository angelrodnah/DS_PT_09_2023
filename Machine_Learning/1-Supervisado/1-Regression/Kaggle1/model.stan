
data {
  int<lower=0> N;        // number of observations
  int<lower=0> K;        // number of predictors
  matrix[N, K] X;        // predictor matrix
  int<lower=0> y[N];      // response variable
}

parameters {
  real alpha;             // intercept
  vector[K] beta;         // coefficients
}

model {
  vector[N] mu;
  alpha ~ normal(0, 10);
  beta ~ normal(0, 1);

  mu = exp(alpha + X * beta);
  y ~ neg_binomial_2(mu, 1);  // Negative binomial likelihood
}
