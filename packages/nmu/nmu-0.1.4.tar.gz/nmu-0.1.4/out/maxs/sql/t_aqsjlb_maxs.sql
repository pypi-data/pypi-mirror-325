CREATE TABLE usr_netsec.t_aqsjlb_maxs
(
    riskLevel int,
    riskLevelDesc varchar(100),
    quantity bigint,
    securityEventTypeId varchar(100),
    securityEventType varchar(100),
    eventQuantity bigint,
    ts bigint    NOT NULL DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP) * 1000,
    PRIMARY KEY (ts)
);

-- 为字段添加注释
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.riskLevel IS '风险等级排名';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.riskLevelDesc IS '风险等级说明';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.quantity IS '数量';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.securityEventTypeId IS '安全事件类型id';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.securityEventType IS '安全事件类型';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.eventQuantity IS '事件数量';
COMMENT ON COLUMN usr_netsec.t_aqsjlb_maxs.ts IS '入库时间';

-- 为表添加注释
COMMENT ON TABLE usr_netsec.t_aqsjlb_maxs IS '安全事件列表';

ALTER TABLE usr_netsec.t_aqsjlb_maxs
    OWNER TO usr_netsec;