marsbar('on')

i = 1

for x = -70:6:73
    for y = -106:6:75
        for z = -70:6:81
            my_centers(i,1) = x;
            my_centers(i,2) = y;
            my_centers(i,3) = z;
            i = i + 1;
        end
    end
end

radius = 3;
roi_dir = '/data/mridata/jdeng/sd_bvftd/nodes/all_nodes_2';

for pt_no = 1:size(my_centers, 1)
    params = struct('centre', my_centers(pt_no, :), 'radius', radius);
    roi = maroi_sphere(params);
    save_as_image(roi, fullfile(roi_dir, sprintf('node_%d.nii', pt_no)));
end
