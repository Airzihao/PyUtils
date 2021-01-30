import os



if __name__ == '__main__':
    scaleFactorList = ['0.003', '0.1', '0.3','1', '3', '10']
    src_ldbc = "/home/zzh/src-ldbc"
    dynamic_path = "/home/zzh/src-ldbc/social_network/dynamic"
    static_path = "home/zzh/src-ldbc/social_network/static"

    for scaleFactor in scaleFactorList:
        output_dir = os.path.join(src_ldbc, "ldbc-{}".format(scaleFactor))
        os.system("mkdir {}".format(output_dir))
        cmd1 = "/home/zzh/src-ldbc/tools/run.py --cores 56 --memory 180g /home/zzh/src-ldbc/target/ldbc_snb_datagen-0.4.0-SNAPSHOT-jar-with-dependencies.jar params/params-{}.ini".format(scaleFactor)
        os.system(cmd1)