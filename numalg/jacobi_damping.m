% -----------------------------------------------
% Newton's Method with Dämpfung
% -----------------------------------------------

n = 3;  % number of variables / equations

% --- Define F(x) ---
F{1} = @(x) x(1)*x(2)*x(3)+x(1)*x(2)+1;
F{2} = @(x) (x(1)^2) + (x(2)^2) + x(2)*x(3) - 1;
F{3} = @(x) 2*x(1)-(x(3)^3) - x(2);

% --- Define Jacobian ---
J{1,1} = @(x) x(2)*x(3)+x(2);
J{1,2} = @(x) x(1)*x(3)+x(1);
J{1,3} = @(x) x(1)*x(2);
J{2,1} = @(x) 2*x(1);
J{2,2} = @(x) 2*x(2)+x(3);
J{2,3} = @(x) x(2);
J{3,1} = @(x) 2;
J{3,2} = @(x) -1;
J{3,3} = @(x) -3*x(3)^2;

% --- Initial guess ---
x0 = [];

% --- Damping parameters ---
q    = 0.8;   % reduction factor
jmax = 10;    % max damping iterations

% --- Newton parameters ---
tol     = 1e-10;
maxiter = 2;
x       = x0;

fprintf('\n--- Newton Iteration with Dämpfung ---\n');
fprintf('x0 = [%s]\n\n', num2str(x0.'));

for k = 1:maxiter
  % Evaluate F and its norm at current x
  Fval    = eval_F(x);
  norm_Fk = norm(Fval);

  % Check convergence
  if norm_Fk < tol
    fprintf('Converged after %d steps.\n', k-1);
    fprintf('Solution: x = [%s]\n', num2str(x.'));
    break
  end

  % Evaluate Jacobian
  Jmat = zeros(n, n);
  for i = 1:n
    for j = 1:n
      Jmat(i,j) = J{i,j}(x);
    end
  end

  % Solve J * d = -F
  d = Jmat \ (-Fval);

  fprintf('Step %d:\n', k);
  fprintf('  x(k)         = [%s]\n', num2str(x.'));
  fprintf('  F(x(k))      = [%s]\n', num2str(Fval.'));
  fprintf('  ||F(x(k))||  = %e\n',   norm_Fk);
  fprintf('  J(x(k))      =\n'); disp(Jmat);
  fprintf('  d(k)         = [%s]\n', num2str(d.'));

  % --- Dämpfung ---
  for j = 0:jmax
    alpha    = q^j;
    x_new    = x + alpha * d;
    Fval_new = eval_F(x_new);
    norm_Fnew = norm(Fval_new);

    fprintf('    j=%d: alpha=%.6f  ||F(x+alpha*d)|| = %e  (vs ||F(x(k))|| = %e)\n', ...
            j, alpha, norm_Fnew, norm_Fk);

    if norm_Fnew < norm_Fk
      if j > 0
        fprintf('  --> Dämpfung active: accepted j=%d, alpha=%.6f\n', j, alpha);
      end
      break
    end

    if j == jmax
      fprintf('  WARNING: No sufficient alpha found after jmax=%d steps, using alpha=%.6f anyway.\n', jmax, alpha);
    end
  end

  fprintf('  alpha        = %.6f\n', alpha);
  fprintf('  x(k+1)       = [%s]\n', num2str(x_new.'));
  fprintf('  ||F(x(k+1))|| = %e\n\n', norm_Fnew);

  x = x_new;
end

