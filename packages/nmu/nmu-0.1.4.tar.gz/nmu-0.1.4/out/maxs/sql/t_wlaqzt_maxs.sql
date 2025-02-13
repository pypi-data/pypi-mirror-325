CREATE TABLE usr_netsec.t_wlaqzt_maxs
(
    gradeName varchar(255),
    score double precision,
    ts bigint    NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP) * 1000,
    PRIMARY KEY (ts)
);

-- 为字段添加注释
COMMENT ON COLUMN usr_netsec.t_wlaqzt_maxs.gradeName IS '等级名称';
COMMENT ON COLUMN usr_netsec.t_wlaqzt_maxs.score IS '得分';
COMMENT ON COLUMN usr_netsec.t_wlaqzt_maxs.ts IS '入库时间';

-- 为表添加注释
COMMENT ON TABLE usr_netsec.t_wlaqzt_maxs IS '网络安全状态';

ALTER TABLE usr_netsec.t_wlaqzt_maxs
    OWNER TO usr_netsec;