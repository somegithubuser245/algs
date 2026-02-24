% =========================================================
%  Your data
% =========================================================

function A = build_A(x)
  A = [
    ones(size(x)),
    x,
    abs(x)
]';
end



##function A = build_A(x)
##  A = [
##    x,              % w1 * x
##    x.^2,           % w2 * x^2
##    cos(x),         % w3 * cos(x)
##    abs(x),         % w4 * |x|
##    exp(x),         % w5 * e^x
##    log(abs(x)),    % w6 * log|x|  (abs to avoid log of negative)
##    sin(x).^2,      % w7 * sin²(x)
##    ones(size(x))   % w8 * 1  (bias)
##  ];
##end

