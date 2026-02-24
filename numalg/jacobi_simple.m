% -----------------------------------------------
% Newton's Method - Interactive Jacobian Input
% -----------------------------------------------


% -----------------------------------------------
% Newton's Method - Hardcoded System
% -----------------------------------------------

n = 2;  % number of variables / equations

% --- Define F(x) ---
F{1} = @(x) x(1) / (x(2)^3) + exp(x(1) + x(2)) + 1;
F{2} = @(x) (x(1)^2)*(x(2)+3) - 1;

% --- Define Jacobian ---
J{1,1} = @(x) 1/(x(2)^3) + exp(x(1) + x(2));
J{1,2} = @(x) -3*x(1)/(x(2)^4) + exp(x(1) + x(2));
J{2,1} = @(x) 2*x(1)*(x(2)+3);
J{2,2} = @(x) x(1)^2;

% --- Initial guess ---
x0 = [1; -1];


% --- Newton iteration ---
tol     = 1e-10;
maxiter = 50;
x       = x0;

fprintf('\n--- Newton Iteration ---\n');
fprintf('x0 = [%s]\n\n', num2str(x0.'));

for k = 1:maxiter
  % Evaluate F at current x
  Fval = zeros(n, 1);
  for i = 1:n
    Fval(i) = F{i}(x);
  end

  % Evaluate Jacobian matrix at current x
  Jmat = zeros(n, n);
  for i = 1:n
    for j = 1:n
      Jmat(i,j) = J{i,j}(x);
    end
  end

  % Newton step: solve J * delta = -F
  delta = Jmat \ (-Fval);
  x_new = x + delta;

  % Print step result
  fprintf('Step %d:\n', k);
  fprintf('  F(x)    = [%s]\n', num2str(Fval.'));
  fprintf('  ||F(x)|| = %e\n', norm(Fval));
  fprintf('  J(x)    =\n'); disp(Jmat);
  fprintf('  delta   = [%s]\n', num2str(delta.'));
  fprintf('  x_new   = [%s]\n\n', num2str(x_new.'));

  % Check convergence
  if norm(delta) < tol
    fprintf('Converged after %d steps.\n', k);
    fprintf('Solution: x = [%s]\n', num2str(x_new.'));
    break
  end

  x = x_new;
end


