function [d] = DISTEUCLIDIANA(prototipo, objeto)

d = sqrt(sum((objeto - prototipo).^2));

% if(d>1 && d<inf) 
%     disp(sprintf('dist_euclidiana > 0'));
%     d= norma(d);
%     pause;
% end