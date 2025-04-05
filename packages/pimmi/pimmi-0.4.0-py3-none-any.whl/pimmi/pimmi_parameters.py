# dataframe fields
dff_query_id = "query_id"
dff_image_id = "image_id"
dff_twitter_id = "twitter_id"
dff_point_id = "point_id"
dff_image_path = "path"
dff_image_relative_path = "relative_path"
dff_ids = "ids"
dff_desc = "desc"
dff_width = "width"
dff_height = "height"
dff_keep = "keep"
dff_nb_points = "nb_points"
dff_nb_match_total = "nb_match_total"
dff_nb_match_ransac = "nb_match_ransac"
dff_ransac_ratio = "ransac_ratio"
dff_keep_smr = dff_keep + "_smr"
dff_keep_smn = dff_keep + "_smn"
dff_keep_rns = dff_keep + "_rns"
dff_query_pfx = "query_"
dff_result_pfx = "result_"
dff_result_nb_points = dff_result_pfx + dff_nb_points
dff_result_image_id = dff_result_pfx + dff_image_id
dff_result_path = dff_result_pfx + dff_image_path
dff_result_width = dff_result_pfx + dff_width
dff_result_height = dff_result_pfx + dff_height
dff_query_nb_points = dff_query_pfx + dff_nb_points
dff_query_image_id = dff_query_pfx + dff_image_id
dff_query_path = dff_query_pfx + dff_image_path
dff_query_width = dff_query_pfx + dff_width
dff_query_height = dff_query_pfx + dff_height
dff_pack_id = "id"
dff_pack_files = "files"

mex_id = "id"
mex_relative_path = "relativePath"
mex_ext_retrieved = "extRetrieved"
mex_ext_unknown_id = "extIsUnknownId"
mex_ext_locked_id = "extIsLockedId"
mex_ext_over_capacity = "extIsOverCapacity"
mex_ext_need_retrieve = "extNeedToRetrieve"
mex_ext_file_type = "fileType"
mex_ext_media_url = "mediaUrl"
mex_ext_first_seen = "firstSeen"
mex_ext_at_least_one_french = "atLeastOneFrench"
mex_nbSeen = "nbSeen"
mex_sha256 = "sha256"

query_fieldnames = ['pack_id', 'query_image_id', 'result_image_id', 'query_path', 'result_path', 'nb_match_total',
                    'nb_match_ransac', 'ransac_ratio', 'query_nb_points', 'query_width', 'query_height',
                    'result_nb_points', 'result_width', 'result_height']

# other string constants
cst_stop = "STOP"
