CREATE TABLE usr_netsec.t_zctop5_gjzsj_maxs
(
    srcIp varchar(100),
    srcArea varchar(255),
    dstIpCnt bigint,
    alarmCnt bigint,
    ts bigint    NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP) * 1000,
    PRIMARY KEY (ts)
);

-- 为字段添加注释
COMMENT ON COLUMN usr_netsec.t_zctop5_gjzsj_maxs.srcIp IS '攻击IP';
COMMENT ON COLUMN usr_netsec.t_zctop5_gjzsj_maxs.srcArea IS '攻击者地域';
COMMENT ON COLUMN usr_netsec.t_zctop5_gjzsj_maxs.dstIpCnt IS '受害者数量';
COMMENT ON COLUMN usr_netsec.t_zctop5_gjzsj_maxs.alarmCnt IS '事件数量';
COMMENT ON COLUMN usr_netsec.t_zctop5_gjzsj_maxs.ts IS '入库时间';

-- 为表添加注释
COMMENT ON TABLE usr_netsec.t_zctop5_gjzsj_maxs IS '资产top5攻击者视角';

ALTER TABLE usr_netsec.t_zctop5_gjzsj_maxs
    OWNER TO usr_netsec;