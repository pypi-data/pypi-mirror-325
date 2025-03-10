CREATE TABLE usr_netsec.t_zctop5_shzsj_maxs
(
    ip varchar(100),
    dstAssetName varchar(100),
    dstAssetGroup varchar(255),
    dstAssetOrg varchar(100),
    srcIpCnt bigint,
    alarmCnt bigint,
    ts bigint    NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP) * 1000,
    PRIMARY KEY (ts)
);

-- 为字段添加注释
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.ip IS '受害IP';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.dstAssetName IS '受害资产名称';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.dstAssetGroup IS '受害资产组';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.dstAssetOrg IS '受害组织';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.srcIpCnt IS '攻击者数量';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.alarmCnt IS '事件数量';
COMMENT ON COLUMN usr_netsec.t_zctop5_shzsj_maxs.ts IS '入库时间';

-- 为表添加注释
COMMENT ON TABLE usr_netsec.t_zctop5_shzsj_maxs IS '资产top5受害者视角';

ALTER TABLE usr_netsec.t_zctop5_shzsj_maxs
    OWNER TO usr_netsec;