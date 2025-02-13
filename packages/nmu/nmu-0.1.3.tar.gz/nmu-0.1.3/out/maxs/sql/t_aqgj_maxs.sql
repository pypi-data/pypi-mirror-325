CREATE TABLE usr_netsec.t_aqgj_maxs
(
    pendingCnt bigint,
    solvedCnt bigint,
    ts bigint    NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP) * 1000,
    PRIMARY KEY (ts)
);

-- 为字段添加注释
COMMENT ON COLUMN usr_netsec.t_aqgj_maxs.pendingCnt IS '待处理';
COMMENT ON COLUMN usr_netsec.t_aqgj_maxs.solvedCnt IS '累计处理';
COMMENT ON COLUMN usr_netsec.t_aqgj_maxs.ts IS '入库时间';

-- 为表添加注释
COMMENT ON TABLE usr_netsec.t_aqgj_maxs IS '安全告警';

ALTER TABLE usr_netsec.t_aqgj_maxs
    OWNER TO usr_netsec;