% BUILDING FINGERPRINT MINUTIAE DATABASE
%
% Usage:  build_db(ICount, JCount);
%
% Argument:   ICount -  Number of FingerPrints 
%             JCount -  Number of Images Per FingerPrint
%               

% Vahid. K. Alilou
% Department of Computer Engineering
% The University of Semnan
%
% July 2013
% Icount : 1 - 164
% Jcount : 10

% 
% function build_db()
% 
% cd 'D:\Semesters\Semester - 6\Digital Signal Processing\Project\Help\ROC\Delete\Help1\Fingerprint_Rural_Database';
% files = dir('D:\Semesters\Semester - 6\Digital Signal Processing\Project\Help\ROC\Delete\Help1\Fingerprint_Rural_Database\*.tif');
% file_names = {files.name};
% 
%     for i = 1 : length(file_names)
%     
%         temp = char(file_names(i));
%         img = imread(temp);
% 
%         if ndims(img) == 3; img = rgb2gray(img); end   % colour image
%                 disp(['extracting features from ' temp ' ...']);
%                 ff{i}=ext_finger(img,1);
%     
%     end
%       
%     save('db.mat','ff');
% end

function build_db(ICount, JCount)
    p=0;
 
    for i=1:ICount
        for j=1:JCount
            filename=[ num2str(i) '_' num2str(j) '.tif'];
            
            img = imread(filename); p=p+1;
            if ndims(img) == 3; img = rgb2gray(img); end   % colour image
            disp(['extracting features from ' filename ' ...']);
            ff{p}=ext_finger(img,1);
        end
    end
    save('db.mat','ff');
end