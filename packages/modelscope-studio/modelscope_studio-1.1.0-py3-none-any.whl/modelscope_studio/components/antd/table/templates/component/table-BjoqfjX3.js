import { i as ke, a as z, r as Pe, g as Ne, w as M, b as Le } from "./Index-Dg6GEONj.js";
const T = window.ms_globals.React, Se = window.ms_globals.React.forwardRef, Oe = window.ms_globals.React.useRef, Re = window.ms_globals.React.useState, Te = window.ms_globals.React.useEffect, A = window.ms_globals.React.useMemo, X = window.ms_globals.ReactDOM.createPortal, je = window.ms_globals.internalContext.useContextPropsContext, D = window.ms_globals.internalContext.ContextPropsProvider, N = window.ms_globals.antd.Table, B = window.ms_globals.createItemsContext.createItemsContext;
var Fe = /\s/;
function Ae(t) {
  for (var e = t.length; e-- && Fe.test(t.charAt(e)); )
    ;
  return e;
}
var Me = /^\s+/;
function Ue(t) {
  return t && t.slice(0, Ae(t) + 1).replace(Me, "");
}
var Y = NaN, We = /^[-+]0x[0-9a-f]+$/i, He = /^0b[01]+$/i, De = /^0o[0-7]+$/i, Be = parseInt;
function Z(t) {
  if (typeof t == "number")
    return t;
  if (ke(t))
    return Y;
  if (z(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = z(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = Ue(t);
  var o = He.test(t);
  return o || De.test(t) ? Be(t.slice(2), o ? 2 : 8) : We.test(t) ? Y : +t;
}
var J = function() {
  return Pe.Date.now();
}, Ge = "Expected a function", Je = Math.max, Qe = Math.min;
function Xe(t, e, o) {
  var l, i, n, r, s, a, _ = 0, g = !1, c = !1, w = !0;
  if (typeof t != "function")
    throw new TypeError(Ge);
  e = Z(e) || 0, z(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Je(Z(o.maxWait) || 0, e) : n, w = "trailing" in o ? !!o.trailing : w);
  function u(h) {
    var E = l, O = i;
    return l = i = void 0, _ = h, r = t.apply(O, E), r;
  }
  function b(h) {
    return _ = h, s = setTimeout(p, e), g ? u(h) : r;
  }
  function f(h) {
    var E = h - a, O = h - _, R = e - E;
    return c ? Qe(R, n - O) : R;
  }
  function m(h) {
    var E = h - a, O = h - _;
    return a === void 0 || E >= e || E < 0 || c && O >= n;
  }
  function p() {
    var h = J();
    if (m(h))
      return y(h);
    s = setTimeout(p, f(h));
  }
  function y(h) {
    return s = void 0, w && l ? u(h) : (l = i = void 0, r);
  }
  function v() {
    s !== void 0 && clearTimeout(s), _ = 0, l = a = i = s = void 0;
  }
  function d() {
    return s === void 0 ? r : y(J());
  }
  function S() {
    var h = J(), E = m(h);
    if (l = arguments, i = this, a = h, E) {
      if (s === void 0)
        return b(a);
      if (c)
        return clearTimeout(s), s = setTimeout(p, e), u(a);
    }
    return s === void 0 && (s = setTimeout(p, e)), r;
  }
  return S.cancel = v, S.flush = d, S;
}
var ce = {
  exports: {}
}, G = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ze = T, qe = Symbol.for("react.element"), Ve = Symbol.for("react.fragment"), Ke = Object.prototype.hasOwnProperty, Ye = ze.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ze = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ae(t, e, o) {
  var l, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (l in e) Ke.call(e, l) && !Ze.hasOwnProperty(l) && (i[l] = e[l]);
  if (t && t.defaultProps) for (l in e = t.defaultProps, e) i[l] === void 0 && (i[l] = e[l]);
  return {
    $$typeof: qe,
    type: t,
    key: n,
    ref: r,
    props: i,
    _owner: Ye.current
  };
}
G.Fragment = Ve;
G.jsx = ae;
G.jsxs = ae;
ce.exports = G;
var C = ce.exports;
const {
  SvelteComponent: $e,
  assign: $,
  binding_callbacks: ee,
  check_outros: et,
  children: ue,
  claim_element: de,
  claim_space: tt,
  component_subscribe: te,
  compute_slots: nt,
  create_slot: rt,
  detach: P,
  element: fe,
  empty: ne,
  exclude_internal_props: re,
  get_all_dirty_from_scope: ot,
  get_slot_changes: it,
  group_outros: lt,
  init: st,
  insert_hydration: U,
  safe_not_equal: ct,
  set_custom_element_data: me,
  space: at,
  transition_in: W,
  transition_out: q,
  update_slot_base: ut
} = window.__gradio__svelte__internal, {
  beforeUpdate: dt,
  getContext: ft,
  onDestroy: mt,
  setContext: pt
} = window.__gradio__svelte__internal;
function oe(t) {
  let e, o;
  const l = (
    /*#slots*/
    t[7].default
  ), i = rt(
    l,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = fe("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      e = de(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ue(e);
      i && i.l(r), r.forEach(P), this.h();
    },
    h() {
      me(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      U(n, e, r), i && i.m(e, null), t[9](e), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && ut(
        i,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? it(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : ot(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (W(i, n), o = !0);
    },
    o(n) {
      q(i, n), o = !1;
    },
    d(n) {
      n && P(e), i && i.d(n), t[9](null);
    }
  };
}
function ht(t) {
  let e, o, l, i, n = (
    /*$$slots*/
    t[4].default && oe(t)
  );
  return {
    c() {
      e = fe("react-portal-target"), o = at(), n && n.c(), l = ne(), this.h();
    },
    l(r) {
      e = de(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ue(e).forEach(P), o = tt(r), n && n.l(r), l = ne(), this.h();
    },
    h() {
      me(e, "class", "svelte-1rt0kpf");
    },
    m(r, s) {
      U(r, e, s), t[8](e), U(r, o, s), n && n.m(r, s), U(r, l, s), i = !0;
    },
    p(r, [s]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, s), s & /*$$slots*/
      16 && W(n, 1)) : (n = oe(r), n.c(), W(n, 1), n.m(l.parentNode, l)) : n && (lt(), q(n, 1, 1, () => {
        n = null;
      }), et());
    },
    i(r) {
      i || (W(n), i = !0);
    },
    o(r) {
      q(n), i = !1;
    },
    d(r) {
      r && (P(e), P(o), P(l)), t[8](null), n && n.d(r);
    }
  };
}
function ie(t) {
  const {
    svelteInit: e,
    ...o
  } = t;
  return o;
}
function gt(t, e, o) {
  let l, i, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const s = nt(n);
  let {
    svelteInit: a
  } = e;
  const _ = M(ie(e)), g = M();
  te(t, g, (d) => o(0, l = d));
  const c = M();
  te(t, c, (d) => o(1, i = d));
  const w = [], u = ft("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: f,
    subSlotIndex: m
  } = Ne() || {}, p = a({
    parent: u,
    props: _,
    target: g,
    slot: c,
    slotKey: b,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(d) {
      w.push(d);
    }
  });
  pt("$$ms-gr-react-wrapper", p), dt(() => {
    _.set(ie(e));
  }), mt(() => {
    w.forEach((d) => d());
  });
  function y(d) {
    ee[d ? "unshift" : "push"](() => {
      l = d, g.set(l);
    });
  }
  function v(d) {
    ee[d ? "unshift" : "push"](() => {
      i = d, c.set(i);
    });
  }
  return t.$$set = (d) => {
    o(17, e = $($({}, e), re(d))), "svelteInit" in d && o(5, a = d.svelteInit), "$$scope" in d && o(6, r = d.$$scope);
  }, e = re(e), [l, i, g, c, s, a, r, n, y, v];
}
class _t extends $e {
  constructor(e) {
    super(), st(this, e, gt, ht, ct, {
      svelteInit: 5
    });
  }
}
const le = window.ms_globals.rerender, Q = window.ms_globals.tree;
function wt(t, e = {}) {
  function o(l) {
    const i = M(), n = new _t({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? Q;
          return a.nodes = [...a.nodes, s], le({
            createPortal: X,
            node: Q
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((_) => _.svelteInstance !== i), le({
              createPortal: X,
              node: Q
            });
          }), s;
        },
        ...l.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
const Ct = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function bt(t) {
  return t ? Object.keys(t).reduce((e, o) => {
    const l = t[o];
    return e[o] = xt(o, l), e;
  }, {}) : {};
}
function xt(t, e) {
  return typeof e == "number" && !Ct.includes(t) ? e + "px" : e;
}
function V(t) {
  const e = [], o = t.cloneNode(!1);
  if (t._reactElement) {
    const i = T.Children.toArray(t._reactElement.props.children).map((n) => {
      if (T.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: s
        } = V(n.props.el);
        return T.cloneElement(n, {
          ...n.props,
          el: s,
          children: [...T.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = t._reactElement.props.children, e.push(X(T.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((i) => {
    t.getEventListeners(i).forEach(({
      listener: r,
      type: s,
      useCapture: a
    }) => {
      o.addEventListener(s, r, a);
    });
  });
  const l = Array.from(t.childNodes);
  for (let i = 0; i < l.length; i++) {
    const n = l[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: s
      } = V(n);
      e.push(...s), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: e
  };
}
function Et(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const k = Se(({
  slot: t,
  clone: e,
  className: o,
  style: l,
  observeAttributes: i
}, n) => {
  const r = Oe(), [s, a] = Re([]), {
    forceClone: _
  } = je(), g = _ ? !0 : e;
  return Te(() => {
    var b;
    if (!r.current || !t)
      return;
    let c = t;
    function w() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Et(n, f), o && f.classList.add(...o.split(" ")), l) {
        const m = bt(l);
        Object.keys(m).forEach((p) => {
          f.style[p] = m[p];
        });
      }
    }
    let u = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var v, d, S;
        (v = r.current) != null && v.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: p,
          clonedElement: y
        } = V(t);
        c = y, a(p), c.style.display = "contents", w(), (S = r.current) == null || S.appendChild(c);
      };
      f();
      const m = Xe(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      u = new window.MutationObserver(m), u.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", w(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), u == null || u.disconnect();
    };
  }, [t, g, o, l, n, i]), T.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...s);
});
function yt(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function It(t, e = !1) {
  try {
    if (Le(t))
      return t;
    if (e && !yt(t))
      return;
    if (typeof t == "string") {
      let o = t.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function I(t, e) {
  return A(() => It(t, e), [t, e]);
}
function vt(t) {
  return Object.keys(t).reduce((e, o) => (t[o] !== void 0 && (e[o] = t[o]), e), {});
}
function H(t, e, o) {
  const l = t.filter(Boolean);
  if (l.length !== 0)
    return l.map((i, n) => {
      var _;
      if (typeof i != "object")
        return e != null && e.fallback ? e.fallback(i) : i;
      const r = {
        ...i.props,
        key: ((_ = i.props) == null ? void 0 : _.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let s = r;
      Object.keys(i.slots).forEach((g) => {
        if (!i.slots[g] || !(i.slots[g] instanceof Element) && !i.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((p, y) => {
          s[p] || (s[p] = {}), y !== c.length - 1 && (s = r[p]);
        });
        const w = i.slots[g];
        let u, b, f = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        w instanceof Element ? u = w : (u = w.el, b = w.callback, f = w.clone ?? f, m = w.forceClone ?? m), m = m ?? !!b, s[c[c.length - 1]] = u ? b ? (...p) => (b(c[c.length - 1], p), /* @__PURE__ */ C.jsx(D, {
          params: p,
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(k, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ C.jsx(D, {
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(k, {
            slot: u,
            clone: f
          })
        }) : s[c[c.length - 1]], s = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return i[a] ? r[a] = H(i[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function se(t, e) {
  return t ? /* @__PURE__ */ C.jsx(k, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function j({
  key: t,
  slots: e,
  targets: o
}, l) {
  return e[t] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ C.jsx(D, {
    params: i,
    forceClone: !0,
    children: se(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ C.jsx(D, {
    params: i,
    forceClone: !0,
    children: se(e[t], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  useItems: St,
  withItemsContextProvider: Ot,
  ItemHandler: Lt
} = B("antd-table-columns");
B("antd-table-row-selection-selections");
const {
  useItems: Rt,
  withItemsContextProvider: Tt,
  ItemHandler: jt
} = B("antd-table-row-selection"), {
  useItems: kt,
  withItemsContextProvider: Pt,
  ItemHandler: Ft
} = B("antd-table-expandable");
function F(t) {
  return typeof t == "object" && t !== null ? t : {};
}
const At = wt(Tt(["rowSelection"], Pt(["expandable"], Ot(["default"], ({
  children: t,
  slots: e,
  columns: o,
  getPopupContainer: l,
  pagination: i,
  loading: n,
  rowKey: r,
  rowClassName: s,
  summary: a,
  rowSelection: _,
  expandable: g,
  sticky: c,
  footer: w,
  showSorterTooltip: u,
  onRow: b,
  onHeaderRow: f,
  setSlotParams: m,
  ...p
}) => {
  const {
    items: {
      default: y
    }
  } = St(), {
    items: {
      expandable: v
    }
  } = kt(), {
    items: {
      rowSelection: d
    }
  } = Rt(), S = I(l), h = e["loading.tip"] || e["loading.indicator"], E = F(n), O = e["pagination.showQuickJumper.goButton"] || e["pagination.itemRender"], R = F(i), pe = I(R.showTotal), he = I(s), ge = I(r, !0), _e = e["showSorterTooltip.title"] || typeof u == "object", L = F(u), we = I(L.afterOpenChange), Ce = I(L.getPopupContainer), be = typeof c == "object", K = F(c), xe = I(K.getContainer), Ee = I(b), ye = I(f), Ie = I(a), ve = I(w);
  return /* @__PURE__ */ C.jsxs(C.Fragment, {
    children: [/* @__PURE__ */ C.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ C.jsx(N, {
      ...p,
      columns: A(() => (o == null ? void 0 : o.map((x) => x === "EXPAND_COLUMN" ? N.EXPAND_COLUMN : x === "SELECTION_COLUMN" ? N.SELECTION_COLUMN : x)) || H(y, {
        fallback: (x) => x === "EXPAND_COLUMN" ? N.EXPAND_COLUMN : x === "SELECTION_COLUMN" ? N.SELECTION_COLUMN : x
      }), [y, o]),
      onRow: Ee,
      onHeaderRow: ye,
      summary: e.summary ? j({
        slots: e,
        setSlotParams: m,
        key: "summary"
      }) : Ie,
      rowSelection: A(() => {
        var x;
        return _ || ((x = H(d)) == null ? void 0 : x[0]);
      }, [_, d]),
      expandable: A(() => {
        var x;
        return g || ((x = H(v)) == null ? void 0 : x[0]);
      }, [g, v]),
      rowClassName: he,
      rowKey: ge || r,
      sticky: be ? {
        ...K,
        getContainer: xe
      } : c,
      showSorterTooltip: _e ? {
        ...L,
        afterOpenChange: we,
        getPopupContainer: Ce,
        title: e["showSorterTooltip.title"] ? /* @__PURE__ */ C.jsx(k, {
          slot: e["showSorterTooltip.title"]
        }) : L.title
      } : u,
      pagination: O ? vt({
        ...R,
        showTotal: pe,
        showQuickJumper: e["pagination.showQuickJumper.goButton"] ? {
          goButton: /* @__PURE__ */ C.jsx(k, {
            slot: e["pagination.showQuickJumper.goButton"]
          })
        } : R.showQuickJumper,
        itemRender: e["pagination.itemRender"] ? j({
          slots: e,
          setSlotParams: m,
          key: "pagination.itemRender"
        }) : R.itemRender
      }) : i,
      getPopupContainer: S,
      loading: h ? {
        ...E,
        tip: e["loading.tip"] ? /* @__PURE__ */ C.jsx(k, {
          slot: e["loading.tip"]
        }) : E.tip,
        indicator: e["loading.indicator"] ? /* @__PURE__ */ C.jsx(k, {
          slot: e["loading.indicator"]
        }) : E.indicator
      } : n,
      footer: e.footer ? j({
        slots: e,
        setSlotParams: m,
        key: "footer"
      }) : ve,
      title: e.title ? j({
        slots: e,
        setSlotParams: m,
        key: "title"
      }) : p.title
    })]
  });
}))));
export {
  At as Table,
  At as default
};
