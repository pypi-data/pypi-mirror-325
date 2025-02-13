import { i as dr, a as xt, r as pr, b as hr, g as mr, w as Fe, c as J, d as gr } from "./Index-BKieWp9g.js";
const m = window.ms_globals.React, y = window.ms_globals.React, sr = window.ms_globals.React.forwardRef, Z = window.ms_globals.React.useRef, Rn = window.ms_globals.React.useState, fe = window.ms_globals.React.useEffect, ar = window.ms_globals.React.isValidElement, cr = window.ms_globals.React.useLayoutEffect, lr = window.ms_globals.React.useImperativeHandle, ur = window.ms_globals.React.memo, fr = window.ms_globals.React.useMemo, Ht = window.ms_globals.ReactDOM, St = window.ms_globals.ReactDOM.createPortal, vr = window.ms_globals.internalContext.useContextPropsContext, Vt = window.ms_globals.internalContext.ContextPropsProvider, yr = window.ms_globals.antd.ConfigProvider, Et = window.ms_globals.antd.theme, Mn = window.ms_globals.antd.Button, br = window.ms_globals.antd.Input, Sr = window.ms_globals.antd.Flex, xr = window.ms_globals.antdIcons.CloseOutlined, Er = window.ms_globals.antdIcons.ClearOutlined, Cr = window.ms_globals.antdIcons.ArrowUpOutlined, wr = window.ms_globals.antdIcons.AudioMutedOutlined, _r = window.ms_globals.antdIcons.AudioOutlined, Ct = window.ms_globals.antdCssinjs.unit, ft = window.ms_globals.antdCssinjs.token2CSSVar, Ft = window.ms_globals.antdCssinjs.useStyleRegister, Tr = window.ms_globals.antdCssinjs.useCSSVarRegister, Rr = window.ms_globals.antdCssinjs.createTheme, Mr = window.ms_globals.antdCssinjs.useCacheToken;
var Pr = /\s/;
function Or(e) {
  for (var t = e.length; t-- && Pr.test(e.charAt(t)); )
    ;
  return t;
}
var Ar = /^\s+/;
function kr(e) {
  return e && e.slice(0, Or(e) + 1).replace(Ar, "");
}
var zt = NaN, Lr = /^[-+]0x[0-9a-f]+$/i, Ir = /^0b[01]+$/i, jr = /^0o[0-7]+$/i, Dr = parseInt;
function Xt(e) {
  if (typeof e == "number")
    return e;
  if (dr(e))
    return zt;
  if (xt(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = xt(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = kr(e);
  var n = Ir.test(e);
  return n || jr.test(e) ? Dr(e.slice(2), n ? 2 : 8) : Lr.test(e) ? zt : +e;
}
var dt = function() {
  return pr.Date.now();
}, $r = "Expected a function", Nr = Math.max, Br = Math.min;
function Hr(e, t, n) {
  var o, r, i, s, a, l, c = 0, d = !1, u = !1, f = !0;
  if (typeof e != "function")
    throw new TypeError($r);
  t = Xt(t) || 0, xt(n) && (d = !!n.leading, u = "maxWait" in n, i = u ? Nr(Xt(n.maxWait) || 0, t) : i, f = "trailing" in n ? !!n.trailing : f);
  function h(S) {
    var P = o, O = r;
    return o = r = void 0, c = S, s = e.apply(O, P), s;
  }
  function b(S) {
    return c = S, a = setTimeout(E, t), d ? h(S) : s;
  }
  function p(S) {
    var P = S - l, O = S - c, L = t - P;
    return u ? Br(L, i - O) : L;
  }
  function g(S) {
    var P = S - l, O = S - c;
    return l === void 0 || P >= t || P < 0 || u && O >= i;
  }
  function E() {
    var S = dt();
    if (g(S))
      return _(S);
    a = setTimeout(E, p(S));
  }
  function _(S) {
    return a = void 0, f && o ? h(S) : (o = r = void 0, s);
  }
  function T() {
    a !== void 0 && clearTimeout(a), c = 0, o = l = r = a = void 0;
  }
  function v() {
    return a === void 0 ? s : _(dt());
  }
  function R() {
    var S = dt(), P = g(S);
    if (o = arguments, r = this, l = S, P) {
      if (a === void 0)
        return b(l);
      if (u)
        return clearTimeout(a), a = setTimeout(E, t), h(l);
    }
    return a === void 0 && (a = setTimeout(E, t)), s;
  }
  return R.cancel = T, R.flush = v, R;
}
function Vr(e, t) {
  return hr(e, t);
}
var Pn = {
  exports: {}
}, Ge = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Fr = y, zr = Symbol.for("react.element"), Xr = Symbol.for("react.fragment"), Ur = Object.prototype.hasOwnProperty, Wr = Fr.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Kr = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function On(e, t, n) {
  var o, r = {}, i = null, s = null;
  n !== void 0 && (i = "" + n), t.key !== void 0 && (i = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (o in t) Ur.call(t, o) && !Kr.hasOwnProperty(o) && (r[o] = t[o]);
  if (e && e.defaultProps) for (o in t = e.defaultProps, t) r[o] === void 0 && (r[o] = t[o]);
  return {
    $$typeof: zr,
    type: e,
    key: i,
    ref: s,
    props: r,
    _owner: Wr.current
  };
}
Ge.Fragment = Xr;
Ge.jsx = On;
Ge.jsxs = On;
Pn.exports = Ge;
var oe = Pn.exports;
const {
  SvelteComponent: Gr,
  assign: Ut,
  binding_callbacks: Wt,
  check_outros: qr,
  children: An,
  claim_element: kn,
  claim_space: Qr,
  component_subscribe: Kt,
  compute_slots: Yr,
  create_slot: Zr,
  detach: be,
  element: Ln,
  empty: Gt,
  exclude_internal_props: qt,
  get_all_dirty_from_scope: Jr,
  get_slot_changes: eo,
  group_outros: to,
  init: no,
  insert_hydration: ze,
  safe_not_equal: ro,
  set_custom_element_data: In,
  space: oo,
  transition_in: Xe,
  transition_out: wt,
  update_slot_base: io
} = window.__gradio__svelte__internal, {
  beforeUpdate: so,
  getContext: ao,
  onDestroy: co,
  setContext: lo
} = window.__gradio__svelte__internal;
function Qt(e) {
  let t, n;
  const o = (
    /*#slots*/
    e[7].default
  ), r = Zr(
    o,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = Ln("svelte-slot"), r && r.c(), this.h();
    },
    l(i) {
      t = kn(i, "SVELTE-SLOT", {
        class: !0
      });
      var s = An(t);
      r && r.l(s), s.forEach(be), this.h();
    },
    h() {
      In(t, "class", "svelte-1rt0kpf");
    },
    m(i, s) {
      ze(i, t, s), r && r.m(t, null), e[9](t), n = !0;
    },
    p(i, s) {
      r && r.p && (!n || s & /*$$scope*/
      64) && io(
        r,
        o,
        i,
        /*$$scope*/
        i[6],
        n ? eo(
          o,
          /*$$scope*/
          i[6],
          s,
          null
        ) : Jr(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      n || (Xe(r, i), n = !0);
    },
    o(i) {
      wt(r, i), n = !1;
    },
    d(i) {
      i && be(t), r && r.d(i), e[9](null);
    }
  };
}
function uo(e) {
  let t, n, o, r, i = (
    /*$$slots*/
    e[4].default && Qt(e)
  );
  return {
    c() {
      t = Ln("react-portal-target"), n = oo(), i && i.c(), o = Gt(), this.h();
    },
    l(s) {
      t = kn(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), An(t).forEach(be), n = Qr(s), i && i.l(s), o = Gt(), this.h();
    },
    h() {
      In(t, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      ze(s, t, a), e[8](t), ze(s, n, a), i && i.m(s, a), ze(s, o, a), r = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? i ? (i.p(s, a), a & /*$$slots*/
      16 && Xe(i, 1)) : (i = Qt(s), i.c(), Xe(i, 1), i.m(o.parentNode, o)) : i && (to(), wt(i, 1, 1, () => {
        i = null;
      }), qr());
    },
    i(s) {
      r || (Xe(i), r = !0);
    },
    o(s) {
      wt(i), r = !1;
    },
    d(s) {
      s && (be(t), be(n), be(o)), e[8](null), i && i.d(s);
    }
  };
}
function Yt(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function fo(e, t, n) {
  let o, r, {
    $$slots: i = {},
    $$scope: s
  } = t;
  const a = Yr(i);
  let {
    svelteInit: l
  } = t;
  const c = Fe(Yt(t)), d = Fe();
  Kt(e, d, (v) => n(0, o = v));
  const u = Fe();
  Kt(e, u, (v) => n(1, r = v));
  const f = [], h = ao("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: p,
    subSlotIndex: g
  } = mr() || {}, E = l({
    parent: h,
    props: c,
    target: d,
    slot: u,
    slotKey: b,
    slotIndex: p,
    subSlotIndex: g,
    onDestroy(v) {
      f.push(v);
    }
  });
  lo("$$ms-gr-react-wrapper", E), so(() => {
    c.set(Yt(t));
  }), co(() => {
    f.forEach((v) => v());
  });
  function _(v) {
    Wt[v ? "unshift" : "push"](() => {
      o = v, d.set(o);
    });
  }
  function T(v) {
    Wt[v ? "unshift" : "push"](() => {
      r = v, u.set(r);
    });
  }
  return e.$$set = (v) => {
    n(17, t = Ut(Ut({}, t), qt(v))), "svelteInit" in v && n(5, l = v.svelteInit), "$$scope" in v && n(6, s = v.$$scope);
  }, t = qt(t), [o, r, d, u, a, l, s, i, _, T];
}
class po extends Gr {
  constructor(t) {
    super(), no(this, t, fo, uo, ro, {
      svelteInit: 5
    });
  }
}
const Zt = window.ms_globals.rerender, pt = window.ms_globals.tree;
function ho(e, t = {}) {
  function n(o) {
    const r = Fe(), i = new po({
      ...o,
      props: {
        svelteInit(s) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: r,
            reactComponent: e,
            props: s.props,
            slot: s.slot,
            target: s.target,
            slotIndex: s.slotIndex,
            subSlotIndex: s.subSlotIndex,
            ignore: t.ignore,
            slotKey: s.slotKey,
            nodes: []
          }, l = s.parent ?? pt;
          return l.nodes = [...l.nodes, a], Zt({
            createPortal: St,
            node: pt
          }), s.onDestroy(() => {
            l.nodes = l.nodes.filter((c) => c.svelteInstance !== r), Zt({
              createPortal: St,
              node: pt
            });
          }), a;
        },
        ...o.props
      }
    });
    return r.set(i), i;
  }
  return new Promise((o) => {
    window.ms_globals.initializePromise.then(() => {
      o(n);
    });
  });
}
const mo = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function go(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const o = e[n];
    return t[n] = vo(n, o), t;
  }, {}) : {};
}
function vo(e, t) {
  return typeof t == "number" && !mo.includes(e) ? t + "px" : t;
}
function _t(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const r = y.Children.toArray(e._reactElement.props.children).map((i) => {
      if (y.isValidElement(i) && i.props.__slot__) {
        const {
          portals: s,
          clonedElement: a
        } = _t(i.props.el);
        return y.cloneElement(i, {
          ...i.props,
          el: a,
          children: [...y.Children.toArray(i.props.children), ...s]
        });
      }
      return null;
    });
    return r.originalChildren = e._reactElement.props.children, t.push(St(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: r
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((r) => {
    e.getEventListeners(r).forEach(({
      listener: s,
      type: a,
      useCapture: l
    }) => {
      n.addEventListener(a, s, l);
    });
  });
  const o = Array.from(e.childNodes);
  for (let r = 0; r < o.length; r++) {
    const i = o[r];
    if (i.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = _t(i);
      t.push(...a), n.appendChild(s);
    } else i.nodeType === 3 && n.appendChild(i.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function yo(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Tt = sr(({
  slot: e,
  clone: t,
  className: n,
  style: o,
  observeAttributes: r
}, i) => {
  const s = Z(), [a, l] = Rn([]), {
    forceClone: c
  } = vr(), d = c ? !0 : t;
  return fe(() => {
    var b;
    if (!s.current || !e)
      return;
    let u = e;
    function f() {
      let p = u;
      if (u.tagName.toLowerCase() === "svelte-slot" && u.children.length === 1 && u.children[0] && (p = u.children[0], p.tagName.toLowerCase() === "react-portal-target" && p.children[0] && (p = p.children[0])), yo(i, p), n && p.classList.add(...n.split(" ")), o) {
        const g = go(o);
        Object.keys(g).forEach((E) => {
          p.style[E] = g[E];
        });
      }
    }
    let h = null;
    if (d && window.MutationObserver) {
      let p = function() {
        var T, v, R;
        (T = s.current) != null && T.contains(u) && ((v = s.current) == null || v.removeChild(u));
        const {
          portals: E,
          clonedElement: _
        } = _t(e);
        u = _, l(E), u.style.display = "contents", f(), (R = s.current) == null || R.appendChild(u);
      };
      p();
      const g = Hr(() => {
        p(), h == null || h.disconnect(), h == null || h.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: r
        });
      }, 50);
      h = new window.MutationObserver(g), h.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      u.style.display = "contents", f(), (b = s.current) == null || b.appendChild(u);
    return () => {
      var p, g;
      u.style.display = "", (p = s.current) != null && p.contains(u) && ((g = s.current) == null || g.removeChild(u)), h == null || h.disconnect();
    };
  }, [e, d, n, o, i, r]), y.createElement("react-child", {
    ref: s,
    style: {
      display: "contents"
    }
  }, ...a);
}), bo = "1.0.5", So = /* @__PURE__ */ y.createContext({}), xo = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, Eo = (e) => {
  const t = y.useContext(So);
  return y.useMemo(() => ({
    ...xo,
    ...t[e]
  }), [t[e]]);
};
function se() {
  return se = Object.assign ? Object.assign.bind() : function(e) {
    for (var t = 1; t < arguments.length; t++) {
      var n = arguments[t];
      for (var o in n) ({}).hasOwnProperty.call(n, o) && (e[o] = n[o]);
    }
    return e;
  }, se.apply(null, arguments);
}
function Rt() {
  const {
    getPrefixCls: e,
    direction: t,
    csp: n,
    iconPrefixCls: o,
    theme: r
  } = y.useContext(yr.ConfigContext);
  return {
    theme: r,
    getPrefixCls: e,
    direction: t,
    csp: n,
    iconPrefixCls: o
  };
}
function pe(e) {
  var t = m.useRef();
  t.current = e;
  var n = m.useCallback(function() {
    for (var o, r = arguments.length, i = new Array(r), s = 0; s < r; s++)
      i[s] = arguments[s];
    return (o = t.current) === null || o === void 0 ? void 0 : o.call.apply(o, [t].concat(i));
  }, []);
  return n;
}
function Co(e) {
  if (Array.isArray(e)) return e;
}
function wo(e, t) {
  var n = e == null ? null : typeof Symbol < "u" && e[Symbol.iterator] || e["@@iterator"];
  if (n != null) {
    var o, r, i, s, a = [], l = !0, c = !1;
    try {
      if (i = (n = n.call(e)).next, t === 0) {
        if (Object(n) !== n) return;
        l = !1;
      } else for (; !(l = (o = i.call(n)).done) && (a.push(o.value), a.length !== t); l = !0) ;
    } catch (d) {
      c = !0, r = d;
    } finally {
      try {
        if (!l && n.return != null && (s = n.return(), Object(s) !== s)) return;
      } finally {
        if (c) throw r;
      }
    }
    return a;
  }
}
function Jt(e, t) {
  (t == null || t > e.length) && (t = e.length);
  for (var n = 0, o = Array(t); n < t; n++) o[n] = e[n];
  return o;
}
function _o(e, t) {
  if (e) {
    if (typeof e == "string") return Jt(e, t);
    var n = {}.toString.call(e).slice(8, -1);
    return n === "Object" && e.constructor && (n = e.constructor.name), n === "Map" || n === "Set" ? Array.from(e) : n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? Jt(e, t) : void 0;
  }
}
function To() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function X(e, t) {
  return Co(e) || wo(e, t) || _o(e, t) || To();
}
function qe() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var en = qe() ? m.useLayoutEffect : m.useEffect, Ro = function(t, n) {
  var o = m.useRef(!0);
  en(function() {
    return t(o.current);
  }, n), en(function() {
    return o.current = !1, function() {
      o.current = !0;
    };
  }, []);
}, tn = function(t, n) {
  Ro(function(o) {
    if (!o)
      return t();
  }, n);
};
function Ae(e) {
  var t = m.useRef(!1), n = m.useState(e), o = X(n, 2), r = o[0], i = o[1];
  m.useEffect(function() {
    return t.current = !1, function() {
      t.current = !0;
    };
  }, []);
  function s(a, l) {
    l && t.current || i(a);
  }
  return [r, s];
}
function ht(e) {
  return e !== void 0;
}
function jn(e, t) {
  var n = t || {}, o = n.defaultValue, r = n.value, i = n.onChange, s = n.postState, a = Ae(function() {
    return ht(r) ? r : ht(o) ? typeof o == "function" ? o() : o : typeof e == "function" ? e() : e;
  }), l = X(a, 2), c = l[0], d = l[1], u = r !== void 0 ? r : c, f = s ? s(u) : u, h = pe(i), b = Ae([u]), p = X(b, 2), g = p[0], E = p[1];
  tn(function() {
    var T = g[0];
    c !== T && h(c, T);
  }, [g]), tn(function() {
    ht(r) || d(r);
  }, [r]);
  var _ = pe(function(T, v) {
    d(T, v), E([u], v);
  });
  return [f, _];
}
function z(e) {
  "@babel/helpers - typeof";
  return z = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(t) {
    return typeof t;
  } : function(t) {
    return t && typeof Symbol == "function" && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t;
  }, z(e);
}
var Dn = {
  exports: {}
}, A = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var jt = Symbol.for("react.element"), Dt = Symbol.for("react.portal"), Qe = Symbol.for("react.fragment"), Ye = Symbol.for("react.strict_mode"), Ze = Symbol.for("react.profiler"), Je = Symbol.for("react.provider"), et = Symbol.for("react.context"), Mo = Symbol.for("react.server_context"), tt = Symbol.for("react.forward_ref"), nt = Symbol.for("react.suspense"), rt = Symbol.for("react.suspense_list"), ot = Symbol.for("react.memo"), it = Symbol.for("react.lazy"), Po = Symbol.for("react.offscreen"), $n;
$n = Symbol.for("react.module.reference");
function W(e) {
  if (typeof e == "object" && e !== null) {
    var t = e.$$typeof;
    switch (t) {
      case jt:
        switch (e = e.type, e) {
          case Qe:
          case Ze:
          case Ye:
          case nt:
          case rt:
            return e;
          default:
            switch (e = e && e.$$typeof, e) {
              case Mo:
              case et:
              case tt:
              case it:
              case ot:
              case Je:
                return e;
              default:
                return t;
            }
        }
      case Dt:
        return t;
    }
  }
}
A.ContextConsumer = et;
A.ContextProvider = Je;
A.Element = jt;
A.ForwardRef = tt;
A.Fragment = Qe;
A.Lazy = it;
A.Memo = ot;
A.Portal = Dt;
A.Profiler = Ze;
A.StrictMode = Ye;
A.Suspense = nt;
A.SuspenseList = rt;
A.isAsyncMode = function() {
  return !1;
};
A.isConcurrentMode = function() {
  return !1;
};
A.isContextConsumer = function(e) {
  return W(e) === et;
};
A.isContextProvider = function(e) {
  return W(e) === Je;
};
A.isElement = function(e) {
  return typeof e == "object" && e !== null && e.$$typeof === jt;
};
A.isForwardRef = function(e) {
  return W(e) === tt;
};
A.isFragment = function(e) {
  return W(e) === Qe;
};
A.isLazy = function(e) {
  return W(e) === it;
};
A.isMemo = function(e) {
  return W(e) === ot;
};
A.isPortal = function(e) {
  return W(e) === Dt;
};
A.isProfiler = function(e) {
  return W(e) === Ze;
};
A.isStrictMode = function(e) {
  return W(e) === Ye;
};
A.isSuspense = function(e) {
  return W(e) === nt;
};
A.isSuspenseList = function(e) {
  return W(e) === rt;
};
A.isValidElementType = function(e) {
  return typeof e == "string" || typeof e == "function" || e === Qe || e === Ze || e === Ye || e === nt || e === rt || e === Po || typeof e == "object" && e !== null && (e.$$typeof === it || e.$$typeof === ot || e.$$typeof === Je || e.$$typeof === et || e.$$typeof === tt || e.$$typeof === $n || e.getModuleId !== void 0);
};
A.typeOf = W;
Dn.exports = A;
var mt = Dn.exports, Oo = Symbol.for("react.element"), Ao = Symbol.for("react.transitional.element"), ko = Symbol.for("react.fragment");
function Lo(e) {
  return (
    // Base object type
    e && z(e) === "object" && // React Element type
    (e.$$typeof === Oo || e.$$typeof === Ao) && // React Fragment type
    e.type === ko
  );
}
var Io = function(t, n) {
  typeof t == "function" ? t(n) : z(t) === "object" && t && "current" in t && (t.current = n);
}, jo = function(t) {
  var n, o;
  if (!t)
    return !1;
  if (Nn(t) && t.props.propertyIsEnumerable("ref"))
    return !0;
  var r = mt.isMemo(t) ? t.type.type : t.type;
  return !(typeof r == "function" && !((n = r.prototype) !== null && n !== void 0 && n.render) && r.$$typeof !== mt.ForwardRef || typeof t == "function" && !((o = t.prototype) !== null && o !== void 0 && o.render) && t.$$typeof !== mt.ForwardRef);
};
function Nn(e) {
  return /* @__PURE__ */ ar(e) && !Lo(e);
}
var Do = function(t) {
  if (t && Nn(t)) {
    var n = t;
    return n.props.propertyIsEnumerable("ref") ? n.props.ref : n.ref;
  }
  return null;
};
function $o(e, t) {
  for (var n = e, o = 0; o < t.length; o += 1) {
    if (n == null)
      return;
    n = n[t[o]];
  }
  return n;
}
function No(e, t) {
  if (z(e) != "object" || !e) return e;
  var n = e[Symbol.toPrimitive];
  if (n !== void 0) {
    var o = n.call(e, t || "default");
    if (z(o) != "object") return o;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (t === "string" ? String : Number)(e);
}
function Bn(e) {
  var t = No(e, "string");
  return z(t) == "symbol" ? t : t + "";
}
function w(e, t, n) {
  return (t = Bn(t)) in e ? Object.defineProperty(e, t, {
    value: n,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : e[t] = n, e;
}
function nn(e, t) {
  var n = Object.keys(e);
  if (Object.getOwnPropertySymbols) {
    var o = Object.getOwnPropertySymbols(e);
    t && (o = o.filter(function(r) {
      return Object.getOwnPropertyDescriptor(e, r).enumerable;
    })), n.push.apply(n, o);
  }
  return n;
}
function C(e) {
  for (var t = 1; t < arguments.length; t++) {
    var n = arguments[t] != null ? arguments[t] : {};
    t % 2 ? nn(Object(n), !0).forEach(function(o) {
      w(e, o, n[o]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : nn(Object(n)).forEach(function(o) {
      Object.defineProperty(e, o, Object.getOwnPropertyDescriptor(n, o));
    });
  }
  return e;
}
function rn(e) {
  return e instanceof HTMLElement || e instanceof SVGElement;
}
function Bo(e) {
  return e && z(e) === "object" && rn(e.nativeElement) ? e.nativeElement : rn(e) ? e : null;
}
function Ho(e) {
  var t = Bo(e);
  if (t)
    return t;
  if (e instanceof y.Component) {
    var n;
    return (n = Ht.findDOMNode) === null || n === void 0 ? void 0 : n.call(Ht, e);
  }
  return null;
}
function Vo(e, t) {
  if (e == null) return {};
  var n = {};
  for (var o in e) if ({}.hasOwnProperty.call(e, o)) {
    if (t.includes(o)) continue;
    n[o] = e[o];
  }
  return n;
}
function on(e, t) {
  if (e == null) return {};
  var n, o, r = Vo(e, t);
  if (Object.getOwnPropertySymbols) {
    var i = Object.getOwnPropertySymbols(e);
    for (o = 0; o < i.length; o++) n = i[o], t.includes(n) || {}.propertyIsEnumerable.call(e, n) && (r[n] = e[n]);
  }
  return r;
}
var Fo = /* @__PURE__ */ m.createContext({});
function Ee(e, t) {
  if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function sn(e, t) {
  for (var n = 0; n < t.length; n++) {
    var o = t[n];
    o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(e, Bn(o.key), o);
  }
}
function Ce(e, t, n) {
  return t && sn(e.prototype, t), n && sn(e, n), Object.defineProperty(e, "prototype", {
    writable: !1
  }), e;
}
function Mt(e, t) {
  return Mt = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(n, o) {
    return n.__proto__ = o, n;
  }, Mt(e, t);
}
function st(e, t) {
  if (typeof t != "function" && t !== null) throw new TypeError("Super expression must either be null or a function");
  e.prototype = Object.create(t && t.prototype, {
    constructor: {
      value: e,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(e, "prototype", {
    writable: !1
  }), t && Mt(e, t);
}
function We(e) {
  return We = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
    return t.__proto__ || Object.getPrototypeOf(t);
  }, We(e);
}
function Hn() {
  try {
    var e = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (Hn = function() {
    return !!e;
  })();
}
function de(e) {
  if (e === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return e;
}
function zo(e, t) {
  if (t && (z(t) == "object" || typeof t == "function")) return t;
  if (t !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return de(e);
}
function at(e) {
  var t = Hn();
  return function() {
    var n, o = We(e);
    if (t) {
      var r = We(this).constructor;
      n = Reflect.construct(o, arguments, r);
    } else n = o.apply(this, arguments);
    return zo(this, n);
  };
}
var Xo = /* @__PURE__ */ function(e) {
  st(n, e);
  var t = at(n);
  function n() {
    return Ee(this, n), t.apply(this, arguments);
  }
  return Ce(n, [{
    key: "render",
    value: function() {
      return this.props.children;
    }
  }]), n;
}(m.Component);
function Uo(e) {
  var t = m.useReducer(function(a) {
    return a + 1;
  }, 0), n = X(t, 2), o = n[1], r = m.useRef(e), i = pe(function() {
    return r.current;
  }), s = pe(function(a) {
    r.current = typeof a == "function" ? a(r.current) : a, o();
  });
  return [i, s];
}
var ue = "none", je = "appear", De = "enter", $e = "leave", an = "none", G = "prepare", Se = "start", xe = "active", $t = "end", Vn = "prepared";
function cn(e, t) {
  var n = {};
  return n[e.toLowerCase()] = t.toLowerCase(), n["Webkit".concat(e)] = "webkit".concat(t), n["Moz".concat(e)] = "moz".concat(t), n["ms".concat(e)] = "MS".concat(t), n["O".concat(e)] = "o".concat(t.toLowerCase()), n;
}
function Wo(e, t) {
  var n = {
    animationend: cn("Animation", "AnimationEnd"),
    transitionend: cn("Transition", "TransitionEnd")
  };
  return e && ("AnimationEvent" in t || delete n.animationend.animation, "TransitionEvent" in t || delete n.transitionend.transition), n;
}
var Ko = Wo(qe(), typeof window < "u" ? window : {}), Fn = {};
if (qe()) {
  var Go = document.createElement("div");
  Fn = Go.style;
}
var Ne = {};
function zn(e) {
  if (Ne[e])
    return Ne[e];
  var t = Ko[e];
  if (t)
    for (var n = Object.keys(t), o = n.length, r = 0; r < o; r += 1) {
      var i = n[r];
      if (Object.prototype.hasOwnProperty.call(t, i) && i in Fn)
        return Ne[e] = t[i], Ne[e];
    }
  return "";
}
var Xn = zn("animationend"), Un = zn("transitionend"), Wn = !!(Xn && Un), ln = Xn || "animationend", un = Un || "transitionend";
function fn(e, t) {
  if (!e) return null;
  if (z(e) === "object") {
    var n = t.replace(/-\w/g, function(o) {
      return o[1].toUpperCase();
    });
    return e[n];
  }
  return "".concat(e, "-").concat(t);
}
const qo = function(e) {
  var t = Z();
  function n(r) {
    r && (r.removeEventListener(un, e), r.removeEventListener(ln, e));
  }
  function o(r) {
    t.current && t.current !== r && n(t.current), r && r !== t.current && (r.addEventListener(un, e), r.addEventListener(ln, e), t.current = r);
  }
  return m.useEffect(function() {
    return function() {
      n(t.current);
    };
  }, []), [o, n];
};
var Kn = qe() ? cr : fe, Gn = function(t) {
  return +setTimeout(t, 16);
}, qn = function(t) {
  return clearTimeout(t);
};
typeof window < "u" && "requestAnimationFrame" in window && (Gn = function(t) {
  return window.requestAnimationFrame(t);
}, qn = function(t) {
  return window.cancelAnimationFrame(t);
});
var dn = 0, Nt = /* @__PURE__ */ new Map();
function Qn(e) {
  Nt.delete(e);
}
var Pt = function(t) {
  var n = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 1;
  dn += 1;
  var o = dn;
  function r(i) {
    if (i === 0)
      Qn(o), t();
    else {
      var s = Gn(function() {
        r(i - 1);
      });
      Nt.set(o, s);
    }
  }
  return r(n), o;
};
Pt.cancel = function(e) {
  var t = Nt.get(e);
  return Qn(e), qn(t);
};
const Qo = function() {
  var e = m.useRef(null);
  function t() {
    Pt.cancel(e.current);
  }
  function n(o) {
    var r = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 2;
    t();
    var i = Pt(function() {
      r <= 1 ? o({
        isCanceled: function() {
          return i !== e.current;
        }
      }) : n(o, r - 1);
    });
    e.current = i;
  }
  return m.useEffect(function() {
    return function() {
      t();
    };
  }, []), [n, t];
};
var Yo = [G, Se, xe, $t], Zo = [G, Vn], Yn = !1, Jo = !0;
function Zn(e) {
  return e === xe || e === $t;
}
const ei = function(e, t, n) {
  var o = Ae(an), r = X(o, 2), i = r[0], s = r[1], a = Qo(), l = X(a, 2), c = l[0], d = l[1];
  function u() {
    s(G, !0);
  }
  var f = t ? Zo : Yo;
  return Kn(function() {
    if (i !== an && i !== $t) {
      var h = f.indexOf(i), b = f[h + 1], p = n(i);
      p === Yn ? s(b, !0) : b && c(function(g) {
        function E() {
          g.isCanceled() || s(b, !0);
        }
        p === !0 ? E() : Promise.resolve(p).then(E);
      });
    }
  }, [e, i]), m.useEffect(function() {
    return function() {
      d();
    };
  }, []), [u, i];
};
function ti(e, t, n, o) {
  var r = o.motionEnter, i = r === void 0 ? !0 : r, s = o.motionAppear, a = s === void 0 ? !0 : s, l = o.motionLeave, c = l === void 0 ? !0 : l, d = o.motionDeadline, u = o.motionLeaveImmediately, f = o.onAppearPrepare, h = o.onEnterPrepare, b = o.onLeavePrepare, p = o.onAppearStart, g = o.onEnterStart, E = o.onLeaveStart, _ = o.onAppearActive, T = o.onEnterActive, v = o.onLeaveActive, R = o.onAppearEnd, S = o.onEnterEnd, P = o.onLeaveEnd, O = o.onVisibleChanged, L = Ae(), B = X(L, 2), $ = B[0], k = B[1], M = Uo(ue), I = X(M, 2), j = I[0], N = I[1], q = Ae(null), Q = X(q, 2), he = Q[0], me = Q[1], U = j(), ee = Z(!1), ae = Z(null);
  function H() {
    return n();
  }
  var te = Z(!1);
  function ce() {
    N(ue), me(null, !0);
  }
  var K = pe(function(V) {
    var x = j();
    if (x !== ue) {
      var D = H();
      if (!(V && !V.deadline && V.target !== D)) {
        var Y = te.current, Ie;
        x === je && Y ? Ie = R == null ? void 0 : R(D, V) : x === De && Y ? Ie = S == null ? void 0 : S(D, V) : x === $e && Y && (Ie = P == null ? void 0 : P(D, V)), Y && Ie !== !1 && ce();
      }
    }
  }), ge = qo(K), ve = X(ge, 1), ye = ve[0], we = function(x) {
    switch (x) {
      case je:
        return w(w(w({}, G, f), Se, p), xe, _);
      case De:
        return w(w(w({}, G, h), Se, g), xe, T);
      case $e:
        return w(w(w({}, G, b), Se, E), xe, v);
      default:
        return {};
    }
  }, ne = m.useMemo(function() {
    return we(U);
  }, [U]), le = ei(U, !e, function(V) {
    if (V === G) {
      var x = ne[G];
      return x ? x(H()) : Yn;
    }
    if (re in ne) {
      var D;
      me(((D = ne[re]) === null || D === void 0 ? void 0 : D.call(ne, H(), null)) || null);
    }
    return re === xe && U !== ue && (ye(H()), d > 0 && (clearTimeout(ae.current), ae.current = setTimeout(function() {
      K({
        deadline: !0
      });
    }, d))), re === Vn && ce(), Jo;
  }), ke = X(le, 2), _e = ke[0], re = ke[1], ut = Zn(re);
  te.current = ut;
  var Le = Z(null);
  Kn(function() {
    if (!(ee.current && Le.current === t)) {
      k(t);
      var V = ee.current;
      ee.current = !0;
      var x;
      !V && t && a && (x = je), V && t && i && (x = De), (V && !t && c || !V && u && !t && c) && (x = $e);
      var D = we(x);
      x && (e || D[G]) ? (N(x), _e()) : N(ue), Le.current = t;
    }
  }, [t]), fe(function() {
    // Cancel appear
    (U === je && !a || // Cancel enter
    U === De && !i || // Cancel leave
    U === $e && !c) && N(ue);
  }, [a, i, c]), fe(function() {
    return function() {
      ee.current = !1, clearTimeout(ae.current);
    };
  }, []);
  var Te = m.useRef(!1);
  fe(function() {
    $ && (Te.current = !0), $ !== void 0 && U === ue && ((Te.current || $) && (O == null || O($)), Te.current = !0);
  }, [$, U]);
  var Re = he;
  return ne[G] && re === Se && (Re = C({
    transition: "none"
  }, Re)), [U, re, Re, $ ?? t];
}
function ni(e) {
  var t = e;
  z(e) === "object" && (t = e.transitionSupport);
  function n(r, i) {
    return !!(r.motionName && t && i !== !1);
  }
  var o = /* @__PURE__ */ m.forwardRef(function(r, i) {
    var s = r.visible, a = s === void 0 ? !0 : s, l = r.removeOnLeave, c = l === void 0 ? !0 : l, d = r.forceRender, u = r.children, f = r.motionName, h = r.leavedClassName, b = r.eventProps, p = m.useContext(Fo), g = p.motion, E = n(r, g), _ = Z(), T = Z();
    function v() {
      try {
        return _.current instanceof HTMLElement ? _.current : Ho(T.current);
      } catch {
        return null;
      }
    }
    var R = ti(E, a, v, r), S = X(R, 4), P = S[0], O = S[1], L = S[2], B = S[3], $ = m.useRef(B);
    B && ($.current = !0);
    var k = m.useCallback(function(Q) {
      _.current = Q, Io(i, Q);
    }, [i]), M, I = C(C({}, b), {}, {
      visible: a
    });
    if (!u)
      M = null;
    else if (P === ue)
      B ? M = u(C({}, I), k) : !c && $.current && h ? M = u(C(C({}, I), {}, {
        className: h
      }), k) : d || !c && !h ? M = u(C(C({}, I), {}, {
        style: {
          display: "none"
        }
      }), k) : M = null;
    else {
      var j;
      O === G ? j = "prepare" : Zn(O) ? j = "active" : O === Se && (j = "start");
      var N = fn(f, "".concat(P, "-").concat(j));
      M = u(C(C({}, I), {}, {
        className: J(fn(f, P), w(w({}, N, N && j), f, typeof f == "string")),
        style: L
      }), k);
    }
    if (/* @__PURE__ */ m.isValidElement(M) && jo(M)) {
      var q = Do(M);
      q || (M = /* @__PURE__ */ m.cloneElement(M, {
        ref: k
      }));
    }
    return /* @__PURE__ */ m.createElement(Xo, {
      ref: T
    }, M);
  });
  return o.displayName = "CSSMotion", o;
}
const Jn = ni(Wn);
var Ot = "add", At = "keep", kt = "remove", gt = "removed";
function ri(e) {
  var t;
  return e && z(e) === "object" && "key" in e ? t = e : t = {
    key: e
  }, C(C({}, t), {}, {
    key: String(t.key)
  });
}
function Lt() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [];
  return e.map(ri);
}
function oi() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [], t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : [], n = [], o = 0, r = t.length, i = Lt(e), s = Lt(t);
  i.forEach(function(c) {
    for (var d = !1, u = o; u < r; u += 1) {
      var f = s[u];
      if (f.key === c.key) {
        o < u && (n = n.concat(s.slice(o, u).map(function(h) {
          return C(C({}, h), {}, {
            status: Ot
          });
        })), o = u), n.push(C(C({}, f), {}, {
          status: At
        })), o += 1, d = !0;
        break;
      }
    }
    d || n.push(C(C({}, c), {}, {
      status: kt
    }));
  }), o < r && (n = n.concat(s.slice(o).map(function(c) {
    return C(C({}, c), {}, {
      status: Ot
    });
  })));
  var a = {};
  n.forEach(function(c) {
    var d = c.key;
    a[d] = (a[d] || 0) + 1;
  });
  var l = Object.keys(a).filter(function(c) {
    return a[c] > 1;
  });
  return l.forEach(function(c) {
    n = n.filter(function(d) {
      var u = d.key, f = d.status;
      return u !== c || f !== kt;
    }), n.forEach(function(d) {
      d.key === c && (d.status = At);
    });
  }), n;
}
var ii = ["component", "children", "onVisibleChanged", "onAllRemoved"], si = ["status"], ai = ["eventProps", "visible", "children", "motionName", "motionAppear", "motionEnter", "motionLeave", "motionLeaveImmediately", "motionDeadline", "removeOnLeave", "leavedClassName", "onAppearPrepare", "onAppearStart", "onAppearActive", "onAppearEnd", "onEnterStart", "onEnterActive", "onEnterEnd", "onLeaveStart", "onLeaveActive", "onLeaveEnd"];
function ci(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : Jn, n = /* @__PURE__ */ function(o) {
    st(i, o);
    var r = at(i);
    function i() {
      var s;
      Ee(this, i);
      for (var a = arguments.length, l = new Array(a), c = 0; c < a; c++)
        l[c] = arguments[c];
      return s = r.call.apply(r, [this].concat(l)), w(de(s), "state", {
        keyEntities: []
      }), w(de(s), "removeKey", function(d) {
        s.setState(function(u) {
          var f = u.keyEntities.map(function(h) {
            return h.key !== d ? h : C(C({}, h), {}, {
              status: gt
            });
          });
          return {
            keyEntities: f
          };
        }, function() {
          var u = s.state.keyEntities, f = u.filter(function(h) {
            var b = h.status;
            return b !== gt;
          }).length;
          f === 0 && s.props.onAllRemoved && s.props.onAllRemoved();
        });
      }), s;
    }
    return Ce(i, [{
      key: "render",
      value: function() {
        var a = this, l = this.state.keyEntities, c = this.props, d = c.component, u = c.children, f = c.onVisibleChanged;
        c.onAllRemoved;
        var h = on(c, ii), b = d || m.Fragment, p = {};
        return ai.forEach(function(g) {
          p[g] = h[g], delete h[g];
        }), delete h.keys, /* @__PURE__ */ m.createElement(b, h, l.map(function(g, E) {
          var _ = g.status, T = on(g, si), v = _ === Ot || _ === At;
          return /* @__PURE__ */ m.createElement(t, se({}, p, {
            key: T.key,
            visible: v,
            eventProps: T,
            onVisibleChanged: function(S) {
              f == null || f(S, {
                key: T.key
              }), S || a.removeKey(T.key);
            }
          }), function(R, S) {
            return u(C(C({}, R), {}, {
              index: E
            }), S);
          });
        }));
      }
    }], [{
      key: "getDerivedStateFromProps",
      value: function(a, l) {
        var c = a.keys, d = l.keyEntities, u = Lt(c), f = oi(d, u);
        return {
          keyEntities: f.filter(function(h) {
            var b = d.find(function(p) {
              var g = p.key;
              return h.key === g;
            });
            return !(b && b.status === gt && h.status === kt);
          })
        };
      }
    }]), i;
  }(m.Component);
  return w(n, "defaultProps", {
    component: "div"
  }), n;
}
ci(Wn);
var er = /* @__PURE__ */ Ce(function e() {
  Ee(this, e);
}), tr = "CALC_UNIT", li = new RegExp(tr, "g");
function vt(e) {
  return typeof e == "number" ? "".concat(e).concat(tr) : e;
}
var ui = /* @__PURE__ */ function(e) {
  st(n, e);
  var t = at(n);
  function n(o, r) {
    var i;
    Ee(this, n), i = t.call(this), w(de(i), "result", ""), w(de(i), "unitlessCssVar", void 0), w(de(i), "lowPriority", void 0);
    var s = z(o);
    return i.unitlessCssVar = r, o instanceof n ? i.result = "(".concat(o.result, ")") : s === "number" ? i.result = vt(o) : s === "string" && (i.result = o), i;
  }
  return Ce(n, [{
    key: "add",
    value: function(r) {
      return r instanceof n ? this.result = "".concat(this.result, " + ").concat(r.getResult()) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " + ").concat(vt(r))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(r) {
      return r instanceof n ? this.result = "".concat(this.result, " - ").concat(r.getResult()) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " - ").concat(vt(r))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(r) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), r instanceof n ? this.result = "".concat(this.result, " * ").concat(r.getResult(!0)) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " * ").concat(r)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(r) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), r instanceof n ? this.result = "".concat(this.result, " / ").concat(r.getResult(!0)) : (typeof r == "number" || typeof r == "string") && (this.result = "".concat(this.result, " / ").concat(r)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(r) {
      return this.lowPriority || r ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(r) {
      var i = this, s = r || {}, a = s.unit, l = !0;
      return typeof a == "boolean" ? l = a : Array.from(this.unitlessCssVar).some(function(c) {
        return i.result.includes(c);
      }) && (l = !1), this.result = this.result.replace(li, l ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), n;
}(er), fi = /* @__PURE__ */ function(e) {
  st(n, e);
  var t = at(n);
  function n(o) {
    var r;
    return Ee(this, n), r = t.call(this), w(de(r), "result", 0), o instanceof n ? r.result = o.result : typeof o == "number" && (r.result = o), r;
  }
  return Ce(n, [{
    key: "add",
    value: function(r) {
      return r instanceof n ? this.result += r.result : typeof r == "number" && (this.result += r), this;
    }
  }, {
    key: "sub",
    value: function(r) {
      return r instanceof n ? this.result -= r.result : typeof r == "number" && (this.result -= r), this;
    }
  }, {
    key: "mul",
    value: function(r) {
      return r instanceof n ? this.result *= r.result : typeof r == "number" && (this.result *= r), this;
    }
  }, {
    key: "div",
    value: function(r) {
      return r instanceof n ? this.result /= r.result : typeof r == "number" && (this.result /= r), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), n;
}(er), di = function(t, n) {
  var o = t === "css" ? ui : fi;
  return function(r) {
    return new o(r, n);
  };
}, pn = function(t, n) {
  return "".concat([n, t.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function hn(e, t, n, o) {
  var r = C({}, t[e]);
  if (o != null && o.deprecatedTokens) {
    var i = o.deprecatedTokens;
    i.forEach(function(a) {
      var l = X(a, 2), c = l[0], d = l[1];
      if (r != null && r[c] || r != null && r[d]) {
        var u;
        (u = r[d]) !== null && u !== void 0 || (r[d] = r == null ? void 0 : r[c]);
      }
    });
  }
  var s = C(C({}, n), r);
  return Object.keys(s).forEach(function(a) {
    s[a] === t[a] && delete s[a];
  }), s;
}
var nr = typeof CSSINJS_STATISTIC < "u", It = !0;
function Bt() {
  for (var e = arguments.length, t = new Array(e), n = 0; n < e; n++)
    t[n] = arguments[n];
  if (!nr)
    return Object.assign.apply(Object, [{}].concat(t));
  It = !1;
  var o = {};
  return t.forEach(function(r) {
    if (z(r) === "object") {
      var i = Object.keys(r);
      i.forEach(function(s) {
        Object.defineProperty(o, s, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return r[s];
          }
        });
      });
    }
  }), It = !0, o;
}
var mn = {};
function pi() {
}
var hi = function(t) {
  var n, o = t, r = pi;
  return nr && typeof Proxy < "u" && (n = /* @__PURE__ */ new Set(), o = new Proxy(t, {
    get: function(s, a) {
      if (It) {
        var l;
        (l = n) === null || l === void 0 || l.add(a);
      }
      return s[a];
    }
  }), r = function(s, a) {
    var l;
    mn[s] = {
      global: Array.from(n),
      component: C(C({}, (l = mn[s]) === null || l === void 0 ? void 0 : l.component), a)
    };
  }), {
    token: o,
    keys: n,
    flush: r
  };
};
function gn(e, t, n) {
  if (typeof n == "function") {
    var o;
    return n(Bt(t, (o = t[e]) !== null && o !== void 0 ? o : {}));
  }
  return n ?? {};
}
function mi(e) {
  return e === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var n = arguments.length, o = new Array(n), r = 0; r < n; r++)
        o[r] = arguments[r];
      return "max(".concat(o.map(function(i) {
        return Ct(i);
      }).join(","), ")");
    },
    min: function() {
      for (var n = arguments.length, o = new Array(n), r = 0; r < n; r++)
        o[r] = arguments[r];
      return "min(".concat(o.map(function(i) {
        return Ct(i);
      }).join(","), ")");
    }
  };
}
var gi = 1e3 * 60 * 10, vi = /* @__PURE__ */ function() {
  function e() {
    Ee(this, e), w(this, "map", /* @__PURE__ */ new Map()), w(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), w(this, "nextID", 0), w(this, "lastAccessBeat", /* @__PURE__ */ new Map()), w(this, "accessBeat", 0);
  }
  return Ce(e, [{
    key: "set",
    value: function(n, o) {
      this.clear();
      var r = this.getCompositeKey(n);
      this.map.set(r, o), this.lastAccessBeat.set(r, Date.now());
    }
  }, {
    key: "get",
    value: function(n) {
      var o = this.getCompositeKey(n), r = this.map.get(o);
      return this.lastAccessBeat.set(o, Date.now()), this.accessBeat += 1, r;
    }
  }, {
    key: "getCompositeKey",
    value: function(n) {
      var o = this, r = n.map(function(i) {
        return i && z(i) === "object" ? "obj_".concat(o.getObjectID(i)) : "".concat(z(i), "_").concat(i);
      });
      return r.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(n) {
      if (this.objectIDMap.has(n))
        return this.objectIDMap.get(n);
      var o = this.nextID;
      return this.objectIDMap.set(n, o), this.nextID += 1, o;
    }
  }, {
    key: "clear",
    value: function() {
      var n = this;
      if (this.accessBeat > 1e4) {
        var o = Date.now();
        this.lastAccessBeat.forEach(function(r, i) {
          o - r > gi && (n.map.delete(i), n.lastAccessBeat.delete(i));
        }), this.accessBeat = 0;
      }
    }
  }]), e;
}(), vn = new vi();
function yi(e, t) {
  return y.useMemo(function() {
    var n = vn.get(t);
    if (n)
      return n;
    var o = e();
    return vn.set(t, o), o;
  }, t);
}
var bi = function() {
  return {};
};
function Si(e) {
  var t = e.useCSP, n = t === void 0 ? bi : t, o = e.useToken, r = e.usePrefix, i = e.getResetStyles, s = e.getCommonStyle, a = e.getCompUnitless;
  function l(f, h, b, p) {
    var g = Array.isArray(f) ? f[0] : f;
    function E(O) {
      return "".concat(String(g)).concat(O.slice(0, 1).toUpperCase()).concat(O.slice(1));
    }
    var _ = (p == null ? void 0 : p.unitless) || {}, T = typeof a == "function" ? a(f) : {}, v = C(C({}, T), {}, w({}, E("zIndexPopup"), !0));
    Object.keys(_).forEach(function(O) {
      v[E(O)] = _[O];
    });
    var R = C(C({}, p), {}, {
      unitless: v,
      prefixToken: E
    }), S = d(f, h, b, R), P = c(g, b, R);
    return function(O) {
      var L = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : O, B = S(O, L), $ = X(B, 2), k = $[1], M = P(L), I = X(M, 2), j = I[0], N = I[1];
      return [j, k, N];
    };
  }
  function c(f, h, b) {
    var p = b.unitless, g = b.injectStyle, E = g === void 0 ? !0 : g, _ = b.prefixToken, T = b.ignore, v = function(P) {
      var O = P.rootCls, L = P.cssVar, B = L === void 0 ? {} : L, $ = o(), k = $.realToken;
      return Tr({
        path: [f],
        prefix: B.prefix,
        key: B.key,
        unitless: p,
        ignore: T,
        token: k,
        scope: O
      }, function() {
        var M = gn(f, k, h), I = hn(f, k, M, {
          deprecatedTokens: b == null ? void 0 : b.deprecatedTokens
        });
        return Object.keys(M).forEach(function(j) {
          I[_(j)] = I[j], delete I[j];
        }), I;
      }), null;
    }, R = function(P) {
      var O = o(), L = O.cssVar;
      return [function(B) {
        return E && L ? /* @__PURE__ */ y.createElement(y.Fragment, null, /* @__PURE__ */ y.createElement(v, {
          rootCls: P,
          cssVar: L,
          component: f
        }), B) : B;
      }, L == null ? void 0 : L.key];
    };
    return R;
  }
  function d(f, h, b) {
    var p = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, g = Array.isArray(f) ? f : [f, f], E = X(g, 1), _ = E[0], T = g.join("-"), v = e.layer || {
      name: "antd"
    };
    return function(R) {
      var S = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : R, P = o(), O = P.theme, L = P.realToken, B = P.hashId, $ = P.token, k = P.cssVar, M = r(), I = M.rootPrefixCls, j = M.iconPrefixCls, N = n(), q = k ? "css" : "js", Q = yi(function() {
        var H = /* @__PURE__ */ new Set();
        return k && Object.keys(p.unitless || {}).forEach(function(te) {
          H.add(ft(te, k.prefix)), H.add(ft(te, pn(_, k.prefix)));
        }), di(q, H);
      }, [q, _, k == null ? void 0 : k.prefix]), he = mi(q), me = he.max, U = he.min, ee = {
        theme: O,
        token: $,
        hashId: B,
        nonce: function() {
          return N.nonce;
        },
        clientOnly: p.clientOnly,
        layer: v,
        // antd is always at top of styles
        order: p.order || -999
      };
      typeof i == "function" && Ft(C(C({}, ee), {}, {
        clientOnly: !1,
        path: ["Shared", I]
      }), function() {
        return i($, {
          prefix: {
            rootPrefixCls: I,
            iconPrefixCls: j
          },
          csp: N
        });
      });
      var ae = Ft(C(C({}, ee), {}, {
        path: [T, R, j]
      }), function() {
        if (p.injectStyle === !1)
          return [];
        var H = hi($), te = H.token, ce = H.flush, K = gn(_, L, b), ge = ".".concat(R), ve = hn(_, L, K, {
          deprecatedTokens: p.deprecatedTokens
        });
        k && K && z(K) === "object" && Object.keys(K).forEach(function(le) {
          K[le] = "var(".concat(ft(le, pn(_, k.prefix)), ")");
        });
        var ye = Bt(te, {
          componentCls: ge,
          prefixCls: R,
          iconCls: ".".concat(j),
          antCls: ".".concat(I),
          calc: Q,
          // @ts-ignore
          max: me,
          // @ts-ignore
          min: U
        }, k ? K : ve), we = h(ye, {
          hashId: B,
          prefixCls: R,
          rootPrefixCls: I,
          iconPrefixCls: j
        });
        ce(_, ve);
        var ne = typeof s == "function" ? s(ye, R, S, p.resetFont) : null;
        return [p.resetStyle === !1 ? null : ne, we];
      });
      return [ae, B];
    };
  }
  function u(f, h, b) {
    var p = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, g = d(f, h, b, C({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, p)), E = function(T) {
      var v = T.prefixCls, R = T.rootCls, S = R === void 0 ? v : R;
      return g(v, S), null;
    };
    return E;
  }
  return {
    genStyleHooks: l,
    genSubStyleComponent: u,
    genComponentStyleHook: d
  };
}
const F = Math.round;
function yt(e, t) {
  const n = e.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], o = n.map((r) => parseFloat(r));
  for (let r = 0; r < 3; r += 1)
    o[r] = t(o[r] || 0, n[r] || "", r);
  return n[3] ? o[3] = n[3].includes("%") ? o[3] / 100 : o[3] : o[3] = 1, o;
}
const yn = (e, t, n) => n === 0 ? e : e / 100;
function Me(e, t) {
  const n = t || 255;
  return e > n ? n : e < 0 ? 0 : e;
}
class ie {
  constructor(t) {
    w(this, "isValid", !0), w(this, "r", 0), w(this, "g", 0), w(this, "b", 0), w(this, "a", 1), w(this, "_h", void 0), w(this, "_s", void 0), w(this, "_l", void 0), w(this, "_v", void 0), w(this, "_max", void 0), w(this, "_min", void 0), w(this, "_brightness", void 0);
    function n(o) {
      return o[0] in t && o[1] in t && o[2] in t;
    }
    if (t) if (typeof t == "string") {
      let r = function(i) {
        return o.startsWith(i);
      };
      const o = t.trim();
      /^#?[A-F\d]{3,8}$/i.test(o) ? this.fromHexString(o) : r("rgb") ? this.fromRgbString(o) : r("hsl") ? this.fromHslString(o) : (r("hsv") || r("hsb")) && this.fromHsvString(o);
    } else if (t instanceof ie)
      this.r = t.r, this.g = t.g, this.b = t.b, this.a = t.a, this._h = t._h, this._s = t._s, this._l = t._l, this._v = t._v;
    else if (n("rgb"))
      this.r = Me(t.r), this.g = Me(t.g), this.b = Me(t.b), this.a = typeof t.a == "number" ? Me(t.a, 1) : 1;
    else if (n("hsl"))
      this.fromHsl(t);
    else if (n("hsv"))
      this.fromHsv(t);
    else
      throw new Error("@ant-design/fast-color: unsupported input " + JSON.stringify(t));
  }
  // ======================= Setter =======================
  setR(t) {
    return this._sc("r", t);
  }
  setG(t) {
    return this._sc("g", t);
  }
  setB(t) {
    return this._sc("b", t);
  }
  setA(t) {
    return this._sc("a", t, 1);
  }
  setHue(t) {
    const n = this.toHsv();
    return n.h = t, this._c(n);
  }
  // ======================= Getter =======================
  /**
   * Returns the perceived luminance of a color, from 0-1.
   * @see http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
   */
  getLuminance() {
    function t(i) {
      const s = i / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    }
    const n = t(this.r), o = t(this.g), r = t(this.b);
    return 0.2126 * n + 0.7152 * o + 0.0722 * r;
  }
  getHue() {
    if (typeof this._h > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._h = 0 : this._h = F(60 * (this.r === this.getMax() ? (this.g - this.b) / t + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / t + 2 : (this.r - this.g) / t + 4));
    }
    return this._h;
  }
  getSaturation() {
    if (typeof this._s > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._s = 0 : this._s = t / this.getMax();
    }
    return this._s;
  }
  getLightness() {
    return typeof this._l > "u" && (this._l = (this.getMax() + this.getMin()) / 510), this._l;
  }
  getValue() {
    return typeof this._v > "u" && (this._v = this.getMax() / 255), this._v;
  }
  /**
   * Returns the perceived brightness of the color, from 0-255.
   * Note: this is not the b of HSB
   * @see http://www.w3.org/TR/AERT#color-contrast
   */
  getBrightness() {
    return typeof this._brightness > "u" && (this._brightness = (this.r * 299 + this.g * 587 + this.b * 114) / 1e3), this._brightness;
  }
  // ======================== Func ========================
  darken(t = 10) {
    const n = this.getHue(), o = this.getSaturation();
    let r = this.getLightness() - t / 100;
    return r < 0 && (r = 0), this._c({
      h: n,
      s: o,
      l: r,
      a: this.a
    });
  }
  lighten(t = 10) {
    const n = this.getHue(), o = this.getSaturation();
    let r = this.getLightness() + t / 100;
    return r > 1 && (r = 1), this._c({
      h: n,
      s: o,
      l: r,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(t, n = 50) {
    const o = this._c(t), r = n / 100, i = (a) => (o[a] - this[a]) * r + this[a], s = {
      r: F(i("r")),
      g: F(i("g")),
      b: F(i("b")),
      a: F(i("a") * 100) / 100
    };
    return this._c(s);
  }
  /**
   * Mix the color with pure white, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return white.
   */
  tint(t = 10) {
    return this.mix({
      r: 255,
      g: 255,
      b: 255,
      a: 1
    }, t);
  }
  /**
   * Mix the color with pure black, from 0 to 100.
   * Providing 0 will do nothing, providing 100 will always return black.
   */
  shade(t = 10) {
    return this.mix({
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }, t);
  }
  onBackground(t) {
    const n = this._c(t), o = this.a + n.a * (1 - this.a), r = (i) => F((this[i] * this.a + n[i] * n.a * (1 - this.a)) / o);
    return this._c({
      r: r("r"),
      g: r("g"),
      b: r("b"),
      a: o
    });
  }
  // ======================= Status =======================
  isDark() {
    return this.getBrightness() < 128;
  }
  isLight() {
    return this.getBrightness() >= 128;
  }
  // ======================== MISC ========================
  equals(t) {
    return this.r === t.r && this.g === t.g && this.b === t.b && this.a === t.a;
  }
  clone() {
    return this._c(this);
  }
  // ======================= Format =======================
  toHexString() {
    let t = "#";
    const n = (this.r || 0).toString(16);
    t += n.length === 2 ? n : "0" + n;
    const o = (this.g || 0).toString(16);
    t += o.length === 2 ? o : "0" + o;
    const r = (this.b || 0).toString(16);
    if (t += r.length === 2 ? r : "0" + r, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const i = F(this.a * 255).toString(16);
      t += i.length === 2 ? i : "0" + i;
    }
    return t;
  }
  /** CSS support color pattern */
  toHsl() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      l: this.getLightness(),
      a: this.a
    };
  }
  /** CSS support color pattern */
  toHslString() {
    const t = this.getHue(), n = F(this.getSaturation() * 100), o = F(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${t},${n}%,${o}%,${this.a})` : `hsl(${t},${n}%,${o}%)`;
  }
  /** Same as toHsb */
  toHsv() {
    return {
      h: this.getHue(),
      s: this.getSaturation(),
      v: this.getValue(),
      a: this.a
    };
  }
  toRgb() {
    return {
      r: this.r,
      g: this.g,
      b: this.b,
      a: this.a
    };
  }
  toRgbString() {
    return this.a !== 1 ? `rgba(${this.r},${this.g},${this.b},${this.a})` : `rgb(${this.r},${this.g},${this.b})`;
  }
  toString() {
    return this.toRgbString();
  }
  // ====================== Privates ======================
  /** Return a new FastColor object with one channel changed */
  _sc(t, n, o) {
    const r = this.clone();
    return r[t] = Me(n, o), r;
  }
  _c(t) {
    return new this.constructor(t);
  }
  getMax() {
    return typeof this._max > "u" && (this._max = Math.max(this.r, this.g, this.b)), this._max;
  }
  getMin() {
    return typeof this._min > "u" && (this._min = Math.min(this.r, this.g, this.b)), this._min;
  }
  fromHexString(t) {
    const n = t.replace("#", "");
    function o(r, i) {
      return parseInt(n[r] + n[i || r], 16);
    }
    n.length < 6 ? (this.r = o(0), this.g = o(1), this.b = o(2), this.a = n[3] ? o(3) / 255 : 1) : (this.r = o(0, 1), this.g = o(2, 3), this.b = o(4, 5), this.a = n[6] ? o(6, 7) / 255 : 1);
  }
  fromHsl({
    h: t,
    s: n,
    l: o,
    a: r
  }) {
    if (this._h = t % 360, this._s = n, this._l = o, this.a = typeof r == "number" ? r : 1, n <= 0) {
      const f = F(o * 255);
      this.r = f, this.g = f, this.b = f;
    }
    let i = 0, s = 0, a = 0;
    const l = t / 60, c = (1 - Math.abs(2 * o - 1)) * n, d = c * (1 - Math.abs(l % 2 - 1));
    l >= 0 && l < 1 ? (i = c, s = d) : l >= 1 && l < 2 ? (i = d, s = c) : l >= 2 && l < 3 ? (s = c, a = d) : l >= 3 && l < 4 ? (s = d, a = c) : l >= 4 && l < 5 ? (i = d, a = c) : l >= 5 && l < 6 && (i = c, a = d);
    const u = o - c / 2;
    this.r = F((i + u) * 255), this.g = F((s + u) * 255), this.b = F((a + u) * 255);
  }
  fromHsv({
    h: t,
    s: n,
    v: o,
    a: r
  }) {
    this._h = t % 360, this._s = n, this._v = o, this.a = typeof r == "number" ? r : 1;
    const i = F(o * 255);
    if (this.r = i, this.g = i, this.b = i, n <= 0)
      return;
    const s = t / 60, a = Math.floor(s), l = s - a, c = F(o * (1 - n) * 255), d = F(o * (1 - n * l) * 255), u = F(o * (1 - n * (1 - l)) * 255);
    switch (a) {
      case 0:
        this.g = u, this.b = c;
        break;
      case 1:
        this.r = d, this.b = c;
        break;
      case 2:
        this.r = c, this.b = u;
        break;
      case 3:
        this.r = c, this.g = d;
        break;
      case 4:
        this.r = u, this.g = c;
        break;
      case 5:
      default:
        this.g = c, this.b = d;
        break;
    }
  }
  fromHsvString(t) {
    const n = yt(t, yn);
    this.fromHsv({
      h: n[0],
      s: n[1],
      v: n[2],
      a: n[3]
    });
  }
  fromHslString(t) {
    const n = yt(t, yn);
    this.fromHsl({
      h: n[0],
      s: n[1],
      l: n[2],
      a: n[3]
    });
  }
  fromRgbString(t) {
    const n = yt(t, (o, r) => (
      // Convert percentage to number. e.g. 50% -> 128
      r.includes("%") ? F(o / 100 * 255) : o
    ));
    this.r = n[0], this.g = n[1], this.b = n[2], this.a = n[3];
  }
}
const xi = {
  blue: "#1677FF",
  purple: "#722ED1",
  cyan: "#13C2C2",
  green: "#52C41A",
  magenta: "#EB2F96",
  /**
   * @deprecated Use magenta instead
   */
  pink: "#EB2F96",
  red: "#F5222D",
  orange: "#FA8C16",
  yellow: "#FADB14",
  volcano: "#FA541C",
  geekblue: "#2F54EB",
  gold: "#FAAD14",
  lime: "#A0D911"
}, Ei = Object.assign(Object.assign({}, xi), {
  // Color
  colorPrimary: "#1677ff",
  colorSuccess: "#52c41a",
  colorWarning: "#faad14",
  colorError: "#ff4d4f",
  colorInfo: "#1677ff",
  colorLink: "",
  colorTextBase: "",
  colorBgBase: "",
  // Font
  fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial,
'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol',
'Noto Color Emoji'`,
  fontFamilyCode: "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace",
  fontSize: 14,
  // Line
  lineWidth: 1,
  lineType: "solid",
  // Motion
  motionUnit: 0.1,
  motionBase: 0,
  motionEaseOutCirc: "cubic-bezier(0.08, 0.82, 0.17, 1)",
  motionEaseInOutCirc: "cubic-bezier(0.78, 0.14, 0.15, 0.86)",
  motionEaseOut: "cubic-bezier(0.215, 0.61, 0.355, 1)",
  motionEaseInOut: "cubic-bezier(0.645, 0.045, 0.355, 1)",
  motionEaseOutBack: "cubic-bezier(0.12, 0.4, 0.29, 1.46)",
  motionEaseInBack: "cubic-bezier(0.71, -0.46, 0.88, 0.6)",
  motionEaseInQuint: "cubic-bezier(0.755, 0.05, 0.855, 0.06)",
  motionEaseOutQuint: "cubic-bezier(0.23, 1, 0.32, 1)",
  // Radius
  borderRadius: 6,
  // Size
  sizeUnit: 4,
  sizeStep: 4,
  sizePopupArrow: 16,
  // Control Base
  controlHeight: 32,
  // zIndex
  zIndexBase: 0,
  zIndexPopupBase: 1e3,
  // Image
  opacityImage: 1,
  // Wireframe
  wireframe: !1,
  // Motion
  motion: !0
});
function bt(e) {
  return e >= 0 && e <= 255;
}
function Be(e, t) {
  const {
    r: n,
    g: o,
    b: r,
    a: i
  } = new ie(e).toRgb();
  if (i < 1)
    return e;
  const {
    r: s,
    g: a,
    b: l
  } = new ie(t).toRgb();
  for (let c = 0.01; c <= 1; c += 0.01) {
    const d = Math.round((n - s * (1 - c)) / c), u = Math.round((o - a * (1 - c)) / c), f = Math.round((r - l * (1 - c)) / c);
    if (bt(d) && bt(u) && bt(f))
      return new ie({
        r: d,
        g: u,
        b: f,
        a: Math.round(c * 100) / 100
      }).toRgbString();
  }
  return new ie({
    r: n,
    g: o,
    b: r,
    a: 1
  }).toRgbString();
}
var Ci = function(e, t) {
  var n = {};
  for (var o in e) Object.prototype.hasOwnProperty.call(e, o) && t.indexOf(o) < 0 && (n[o] = e[o]);
  if (e != null && typeof Object.getOwnPropertySymbols == "function") for (var r = 0, o = Object.getOwnPropertySymbols(e); r < o.length; r++)
    t.indexOf(o[r]) < 0 && Object.prototype.propertyIsEnumerable.call(e, o[r]) && (n[o[r]] = e[o[r]]);
  return n;
};
function wi(e) {
  const {
    override: t
  } = e, n = Ci(e, ["override"]), o = Object.assign({}, t);
  Object.keys(Ei).forEach((f) => {
    delete o[f];
  });
  const r = Object.assign(Object.assign({}, n), o), i = 480, s = 576, a = 768, l = 992, c = 1200, d = 1600;
  if (r.motion === !1) {
    const f = "0s";
    r.motionDurationFast = f, r.motionDurationMid = f, r.motionDurationSlow = f;
  }
  return Object.assign(Object.assign(Object.assign({}, r), {
    // ============== Background ============== //
    colorFillContent: r.colorFillSecondary,
    colorFillContentHover: r.colorFill,
    colorFillAlter: r.colorFillQuaternary,
    colorBgContainerDisabled: r.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: r.colorBgContainer,
    colorSplit: Be(r.colorBorderSecondary, r.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: r.colorTextQuaternary,
    colorTextDisabled: r.colorTextQuaternary,
    colorTextHeading: r.colorText,
    colorTextLabel: r.colorTextSecondary,
    colorTextDescription: r.colorTextTertiary,
    colorTextLightSolid: r.colorWhite,
    colorHighlight: r.colorError,
    colorBgTextHover: r.colorFillSecondary,
    colorBgTextActive: r.colorFill,
    colorIcon: r.colorTextTertiary,
    colorIconHover: r.colorText,
    colorErrorOutline: Be(r.colorErrorBg, r.colorBgContainer),
    colorWarningOutline: Be(r.colorWarningBg, r.colorBgContainer),
    // Font
    fontSizeIcon: r.fontSizeSM,
    // Line
    lineWidthFocus: r.lineWidth * 3,
    // Control
    lineWidth: r.lineWidth,
    controlOutlineWidth: r.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: r.controlHeight / 2,
    controlItemBgHover: r.colorFillTertiary,
    controlItemBgActive: r.colorPrimaryBg,
    controlItemBgActiveHover: r.colorPrimaryBgHover,
    controlItemBgActiveDisabled: r.colorFill,
    controlTmpOutline: r.colorFillQuaternary,
    controlOutline: Be(r.colorPrimaryBg, r.colorBgContainer),
    lineType: r.lineType,
    borderRadius: r.borderRadius,
    borderRadiusXS: r.borderRadiusXS,
    borderRadiusSM: r.borderRadiusSM,
    borderRadiusLG: r.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: r.sizeXXS,
    paddingXS: r.sizeXS,
    paddingSM: r.sizeSM,
    padding: r.size,
    paddingMD: r.sizeMD,
    paddingLG: r.sizeLG,
    paddingXL: r.sizeXL,
    paddingContentHorizontalLG: r.sizeLG,
    paddingContentVerticalLG: r.sizeMS,
    paddingContentHorizontal: r.sizeMS,
    paddingContentVertical: r.sizeSM,
    paddingContentHorizontalSM: r.size,
    paddingContentVerticalSM: r.sizeXS,
    marginXXS: r.sizeXXS,
    marginXS: r.sizeXS,
    marginSM: r.sizeSM,
    margin: r.size,
    marginMD: r.sizeMD,
    marginLG: r.sizeLG,
    marginXL: r.sizeXL,
    marginXXL: r.sizeXXL,
    boxShadow: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowSecondary: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTertiary: `
      0 1px 2px 0 rgba(0, 0, 0, 0.03),
      0 1px 6px -1px rgba(0, 0, 0, 0.02),
      0 2px 4px 0 rgba(0, 0, 0, 0.02)
    `,
    screenXS: i,
    screenXSMin: i,
    screenXSMax: s - 1,
    screenSM: s,
    screenSMMin: s,
    screenSMMax: a - 1,
    screenMD: a,
    screenMDMin: a,
    screenMDMax: l - 1,
    screenLG: l,
    screenLGMin: l,
    screenLGMax: c - 1,
    screenXL: c,
    screenXLMin: c,
    screenXLMax: d - 1,
    screenXXL: d,
    screenXXLMin: d,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new ie("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new ie("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new ie("rgba(0, 0, 0, 0.09)").toRgbString()}
    `,
    boxShadowDrawerRight: `
      -6px 0 16px 0 rgba(0, 0, 0, 0.08),
      -3px 0 6px -4px rgba(0, 0, 0, 0.12),
      -9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerLeft: `
      6px 0 16px 0 rgba(0, 0, 0, 0.08),
      3px 0 6px -4px rgba(0, 0, 0, 0.12),
      9px 0 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerUp: `
      0 6px 16px 0 rgba(0, 0, 0, 0.08),
      0 3px 6px -4px rgba(0, 0, 0, 0.12),
      0 9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowDrawerDown: `
      0 -6px 16px 0 rgba(0, 0, 0, 0.08),
      0 -3px 6px -4px rgba(0, 0, 0, 0.12),
      0 -9px 28px 8px rgba(0, 0, 0, 0.05)
    `,
    boxShadowTabsOverflowLeft: "inset 10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowRight: "inset -10px 0 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowTop: "inset 0 10px 8px -8px rgba(0, 0, 0, 0.08)",
    boxShadowTabsOverflowBottom: "inset 0 -10px 8px -8px rgba(0, 0, 0, 0.08)"
  }), o);
}
const _i = {
  lineHeight: !0,
  lineHeightSM: !0,
  lineHeightLG: !0,
  lineHeightHeading1: !0,
  lineHeightHeading2: !0,
  lineHeightHeading3: !0,
  lineHeightHeading4: !0,
  lineHeightHeading5: !0,
  opacityLoading: !0,
  fontWeightStrong: !0,
  zIndexPopupBase: !0,
  zIndexBase: !0,
  opacityImage: !0
}, Ti = {
  size: !0,
  sizeSM: !0,
  sizeLG: !0,
  sizeMD: !0,
  sizeXS: !0,
  sizeXXS: !0,
  sizeMS: !0,
  sizeXL: !0,
  sizeXXL: !0,
  sizeUnit: !0,
  sizeStep: !0,
  motionBase: !0,
  motionUnit: !0
}, Ri = Rr(Et.defaultAlgorithm), Mi = {
  screenXS: !0,
  screenXSMin: !0,
  screenXSMax: !0,
  screenSM: !0,
  screenSMMin: !0,
  screenSMMax: !0,
  screenMD: !0,
  screenMDMin: !0,
  screenMDMax: !0,
  screenLG: !0,
  screenLGMin: !0,
  screenLGMax: !0,
  screenXL: !0,
  screenXLMin: !0,
  screenXLMax: !0,
  screenXXL: !0,
  screenXXLMin: !0
}, rr = (e, t, n) => {
  const o = n.getDerivativeToken(e), {
    override: r,
    ...i
  } = t;
  let s = {
    ...o,
    override: r
  };
  return s = wi(s), i && Object.entries(i).forEach(([a, l]) => {
    const {
      theme: c,
      ...d
    } = l;
    let u = d;
    c && (u = rr({
      ...s,
      ...d
    }, {
      override: d
    }, c)), s[a] = u;
  }), s;
};
function Pi() {
  const {
    token: e,
    hashed: t,
    theme: n = Ri,
    override: o,
    cssVar: r
  } = y.useContext(Et._internalContext), [i, s, a] = Mr(n, [Et.defaultSeed, e], {
    salt: `${bo}-${t || ""}`,
    override: o,
    getComputedToken: rr,
    cssVar: r && {
      prefix: r.prefix,
      key: r.key,
      unitless: _i,
      ignore: Ti,
      preserve: Mi
    }
  });
  return [n, a, t ? s : "", i, r];
}
const {
  genStyleHooks: Oi,
  genComponentStyleHook: as,
  genSubStyleComponent: cs
} = Si({
  usePrefix: () => {
    const {
      getPrefixCls: e,
      iconPrefixCls: t
    } = Rt();
    return {
      iconPrefixCls: t,
      rootPrefixCls: e()
    };
  },
  useToken: () => {
    const [e, t, n, o, r] = Pi();
    return {
      theme: e,
      realToken: t,
      hashId: n,
      token: o,
      cssVar: r
    };
  },
  useCSP: () => {
    const {
      csp: e
    } = Rt();
    return e ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
});
var Ai = `accept acceptCharset accessKey action allowFullScreen allowTransparency
    alt async autoComplete autoFocus autoPlay capture cellPadding cellSpacing challenge
    charSet checked classID className colSpan cols content contentEditable contextMenu
    controls coords crossOrigin data dateTime default defer dir disabled download draggable
    encType form formAction formEncType formMethod formNoValidate formTarget frameBorder
    headers height hidden high href hrefLang htmlFor httpEquiv icon id inputMode integrity
    is keyParams keyType kind label lang list loop low manifest marginHeight marginWidth max maxLength media
    mediaGroup method min minLength multiple muted name noValidate nonce open
    optimum pattern placeholder poster preload radioGroup readOnly rel required
    reversed role rowSpan rows sandbox scope scoped scrolling seamless selected
    shape size sizes span spellCheck src srcDoc srcLang srcSet start step style
    summary tabIndex target title type useMap value width wmode wrap`, ki = `onCopy onCut onPaste onCompositionEnd onCompositionStart onCompositionUpdate onKeyDown
    onKeyPress onKeyUp onFocus onBlur onChange onInput onSubmit onClick onContextMenu onDoubleClick
    onDrag onDragEnd onDragEnter onDragExit onDragLeave onDragOver onDragStart onDrop onMouseDown
    onMouseEnter onMouseLeave onMouseMove onMouseOut onMouseOver onMouseUp onSelect onTouchCancel
    onTouchEnd onTouchMove onTouchStart onScroll onWheel onAbort onCanPlay onCanPlayThrough
    onDurationChange onEmptied onEncrypted onEnded onError onLoadedData onLoadedMetadata
    onLoadStart onPause onPlay onPlaying onProgress onRateChange onSeeked onSeeking onStalled onSuspend onTimeUpdate onVolumeChange onWaiting onLoad onError`, Li = "".concat(Ai, " ").concat(ki).split(/[\s\n]+/), Ii = "aria-", ji = "data-";
function bn(e, t) {
  return e.indexOf(t) === 0;
}
function Di(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : !1, n;
  t === !1 ? n = {
    aria: !0,
    data: !0,
    attr: !0
  } : t === !0 ? n = {
    aria: !0
  } : n = C({}, t);
  var o = {};
  return Object.keys(e).forEach(function(r) {
    // Aria
    (n.aria && (r === "role" || bn(r, Ii)) || // Data
    n.data && bn(r, ji) || // Attr
    n.attr && Li.includes(r)) && (o[r] = e[r]);
  }), o;
}
function $i(e, t) {
  return lr(e, () => {
    const n = t(), {
      nativeElement: o
    } = n;
    return new Proxy(o, {
      get(r, i) {
        return n[i] ? n[i] : Reflect.get(r, i);
      }
    });
  });
}
const or = /* @__PURE__ */ m.createContext({}), Sn = () => ({
  height: 0
}), xn = (e) => ({
  height: e.scrollHeight
});
function Ni(e) {
  const {
    title: t,
    onOpenChange: n,
    open: o,
    children: r,
    className: i,
    style: s,
    classNames: a = {},
    styles: l = {},
    closable: c,
    forceRender: d
  } = e, {
    prefixCls: u
  } = m.useContext(or), f = `${u}-header`;
  return /* @__PURE__ */ m.createElement(Jn, {
    motionEnter: !0,
    motionLeave: !0,
    motionName: `${f}-motion`,
    leavedClassName: `${f}-motion-hidden`,
    onEnterStart: Sn,
    onEnterActive: xn,
    onLeaveStart: xn,
    onLeaveActive: Sn,
    visible: o,
    forceRender: d
  }, ({
    className: h,
    style: b
  }) => /* @__PURE__ */ m.createElement("div", {
    className: J(f, h, i),
    style: {
      ...b,
      ...s
    }
  }, (c !== !1 || t) && /* @__PURE__ */ m.createElement("div", {
    className: (
      // We follow antd naming standard here.
      // So the header part is use `-header` suffix.
      // Though its little bit weird for double `-header`.
      J(`${f}-header`, a.header)
    ),
    style: {
      ...l.header
    }
  }, /* @__PURE__ */ m.createElement("div", {
    className: `${f}-title`
  }, t), c !== !1 && /* @__PURE__ */ m.createElement("div", {
    className: `${f}-close`
  }, /* @__PURE__ */ m.createElement(Mn, {
    type: "text",
    icon: /* @__PURE__ */ m.createElement(xr, null),
    size: "small",
    onClick: () => {
      n == null || n(!o);
    }
  }))), r && /* @__PURE__ */ m.createElement("div", {
    className: J(`${f}-content`, a.content),
    style: {
      ...l.content
    }
  }, r)));
}
const ct = /* @__PURE__ */ m.createContext(null);
function Bi(e, t) {
  const {
    className: n,
    action: o,
    onClick: r,
    ...i
  } = e, s = m.useContext(ct), {
    prefixCls: a,
    disabled: l
  } = s, c = s[o], d = l ?? i.disabled ?? s[`${o}Disabled`];
  return /* @__PURE__ */ m.createElement(Mn, se({
    type: "text"
  }, i, {
    ref: t,
    onClick: (u) => {
      d || (c && c(), r && r(u));
    },
    className: J(a, n, {
      [`${a}-disabled`]: d
    })
  }));
}
const lt = /* @__PURE__ */ m.forwardRef(Bi);
function Hi(e, t) {
  return /* @__PURE__ */ m.createElement(lt, se({
    icon: /* @__PURE__ */ m.createElement(Er, null)
  }, e, {
    action: "onClear",
    ref: t
  }));
}
const Vi = /* @__PURE__ */ m.forwardRef(Hi), Fi = /* @__PURE__ */ ur((e) => {
  const {
    className: t
  } = e;
  return /* @__PURE__ */ y.createElement("svg", {
    color: "currentColor",
    viewBox: "0 0 1000 1000",
    xmlns: "http://www.w3.org/2000/svg",
    xmlnsXlink: "http://www.w3.org/1999/xlink",
    className: t
  }, /* @__PURE__ */ y.createElement("title", null, "Stop Loading"), /* @__PURE__ */ y.createElement("rect", {
    fill: "currentColor",
    height: "250",
    rx: "24",
    ry: "24",
    width: "250",
    x: "375",
    y: "375"
  }), /* @__PURE__ */ y.createElement("circle", {
    cx: "500",
    cy: "500",
    fill: "none",
    r: "450",
    stroke: "currentColor",
    strokeWidth: "100",
    opacity: "0.45"
  }), /* @__PURE__ */ y.createElement("circle", {
    cx: "500",
    cy: "500",
    fill: "none",
    r: "450",
    stroke: "currentColor",
    strokeWidth: "100",
    strokeDasharray: "600 9999999"
  }, /* @__PURE__ */ y.createElement("animateTransform", {
    attributeName: "transform",
    dur: "1s",
    from: "0 500 500",
    repeatCount: "indefinite",
    to: "360 500 500",
    type: "rotate"
  })));
});
function zi(e, t) {
  const {
    prefixCls: n
  } = m.useContext(ct), {
    className: o
  } = e;
  return /* @__PURE__ */ m.createElement(lt, se({
    icon: null,
    color: "primary",
    variant: "text",
    shape: "circle"
  }, e, {
    className: J(o, `${n}-loading-button`),
    action: "onCancel",
    ref: t
  }), /* @__PURE__ */ m.createElement(Fi, {
    className: `${n}-loading-icon`
  }));
}
const En = /* @__PURE__ */ m.forwardRef(zi);
function Xi(e, t) {
  return /* @__PURE__ */ m.createElement(lt, se({
    icon: /* @__PURE__ */ m.createElement(Cr, null),
    type: "primary",
    shape: "circle"
  }, e, {
    action: "onSend",
    ref: t
  }));
}
const Cn = /* @__PURE__ */ m.forwardRef(Xi), Pe = 1e3, Oe = 4, Ue = 140, wn = Ue / 2, He = 250, _n = 500, Ve = 0.8;
function Ui({
  className: e
}) {
  return /* @__PURE__ */ y.createElement("svg", {
    color: "currentColor",
    viewBox: `0 0 ${Pe} ${Pe}`,
    xmlns: "http://www.w3.org/2000/svg",
    xmlnsXlink: "http://www.w3.org/1999/xlink",
    className: e
  }, /* @__PURE__ */ y.createElement("title", null, "Speech Recording"), Array.from({
    length: Oe
  }).map((t, n) => {
    const o = (Pe - Ue * Oe) / (Oe - 1), r = n * (o + Ue), i = Pe / 2 - He / 2, s = Pe / 2 - _n / 2;
    return /* @__PURE__ */ y.createElement("rect", {
      fill: "currentColor",
      rx: wn,
      ry: wn,
      height: He,
      width: Ue,
      x: r,
      y: i,
      key: n
    }, /* @__PURE__ */ y.createElement("animate", {
      attributeName: "height",
      values: `${He}; ${_n}; ${He}`,
      keyTimes: "0; 0.5; 1",
      dur: `${Ve}s`,
      begin: `${Ve / Oe * n}s`,
      repeatCount: "indefinite"
    }), /* @__PURE__ */ y.createElement("animate", {
      attributeName: "y",
      values: `${i}; ${s}; ${i}`,
      keyTimes: "0; 0.5; 1",
      dur: `${Ve}s`,
      begin: `${Ve / Oe * n}s`,
      repeatCount: "indefinite"
    }));
  }));
}
function Wi(e, t) {
  const {
    speechRecording: n,
    onSpeechDisabled: o,
    prefixCls: r
  } = m.useContext(ct);
  let i = null;
  return n ? i = /* @__PURE__ */ m.createElement(Ui, {
    className: `${r}-recording-icon`
  }) : o ? i = /* @__PURE__ */ m.createElement(wr, null) : i = /* @__PURE__ */ m.createElement(_r, null), /* @__PURE__ */ m.createElement(lt, se({
    icon: i,
    color: "primary",
    variant: "text"
  }, e, {
    action: "onSpeech",
    ref: t
  }));
}
const Ki = /* @__PURE__ */ m.forwardRef(Wi), Gi = (e) => {
  const {
    componentCls: t,
    calc: n
  } = e, o = `${t}-header`;
  return {
    [t]: {
      [o]: {
        borderBottomWidth: e.lineWidth,
        borderBottomStyle: "solid",
        borderBottomColor: e.colorBorder,
        // ======================== Header ========================
        "&-header": {
          background: e.colorFillAlter,
          fontSize: e.fontSize,
          lineHeight: e.lineHeight,
          paddingBlock: n(e.paddingSM).sub(e.lineWidthBold).equal(),
          paddingInlineStart: e.padding,
          paddingInlineEnd: e.paddingXS,
          display: "flex",
          [`${o}-title`]: {
            flex: "auto"
          }
        },
        // ======================= Content ========================
        "&-content": {
          padding: e.padding
        },
        // ======================== Motion ========================
        "&-motion": {
          transition: ["height", "border"].map((r) => `${r} ${e.motionDurationSlow}`).join(","),
          overflow: "hidden",
          "&-enter-start, &-leave-active": {
            borderBottomColor: "transparent"
          },
          "&-hidden": {
            display: "none"
          }
        }
      }
    }
  };
}, qi = (e) => {
  const {
    componentCls: t,
    padding: n,
    paddingSM: o,
    paddingXS: r,
    lineWidth: i,
    lineWidthBold: s,
    calc: a
  } = e;
  return {
    [t]: {
      position: "relative",
      width: "100%",
      boxSizing: "border-box",
      boxShadow: `${e.boxShadowTertiary}`,
      transition: `background ${e.motionDurationSlow}`,
      // Border
      borderRadius: {
        _skip_check_: !0,
        value: a(e.borderRadius).mul(2).equal()
      },
      borderColor: e.colorBorder,
      borderWidth: 0,
      borderStyle: "solid",
      // Border
      "&:after": {
        content: '""',
        position: "absolute",
        inset: 0,
        pointerEvents: "none",
        transition: `border-color ${e.motionDurationSlow}`,
        borderRadius: {
          _skip_check_: !0,
          value: "inherit"
        },
        borderStyle: "inherit",
        borderColor: "inherit",
        borderWidth: i
      },
      // Focus
      "&:focus-within": {
        boxShadow: `${e.boxShadowSecondary}`,
        borderColor: e.colorPrimary,
        "&:after": {
          borderWidth: s
        }
      },
      "&-disabled": {
        background: e.colorBgContainerDisabled
      },
      // ============================== RTL ==============================
      [`&${t}-rtl`]: {
        direction: "rtl"
      },
      // ============================ Content ============================
      [`${t}-content`]: {
        display: "flex",
        gap: r,
        width: "100%",
        paddingBlock: o,
        paddingInlineStart: n,
        paddingInlineEnd: o,
        boxSizing: "border-box",
        alignItems: "flex-end"
      },
      // ============================ Prefix =============================
      [`${t}-prefix`]: {
        flex: "none"
      },
      // ============================= Input =============================
      [`${t}-input`]: {
        padding: 0,
        borderRadius: 0,
        flex: "auto",
        alignSelf: "center",
        minHeight: "auto"
      },
      // ============================ Actions ============================
      [`${t}-actions-list`]: {
        flex: "none",
        display: "flex",
        "&-presets": {
          gap: e.paddingXS
        }
      },
      [`${t}-actions-btn`]: {
        "&-disabled": {
          opacity: 0.45
        },
        "&-loading-button": {
          padding: 0,
          border: 0
        },
        "&-loading-icon": {
          height: e.controlHeight,
          width: e.controlHeight,
          verticalAlign: "top"
        },
        "&-recording-icon": {
          height: "1.2em",
          width: "1.2em",
          verticalAlign: "top"
        }
      }
    }
  };
}, Qi = () => ({}), Yi = Oi("Sender", (e) => {
  const {
    paddingXS: t,
    calc: n
  } = e, o = Bt(e, {
    SenderContentMaxWidth: `calc(100% - ${Ct(n(t).add(32).equal())})`
  });
  return [qi(o), Gi(o)];
}, Qi);
let Ke;
!Ke && typeof window < "u" && (Ke = window.SpeechRecognition || window.webkitSpeechRecognition);
function Zi(e, t) {
  const n = pe(e), [o, r, i] = y.useMemo(() => typeof t == "object" ? [t.recording, t.onRecordingChange, typeof t.recording == "boolean"] : [void 0, void 0, !1], [t]), [s, a] = y.useState(null);
  y.useEffect(() => {
    if (typeof navigator < "u" && "permissions" in navigator) {
      let p = null;
      return navigator.permissions.query({
        name: "microphone"
      }).then((g) => {
        a(g.state), g.onchange = function() {
          a(this.state);
        }, p = g;
      }), () => {
        p && (p.onchange = null);
      };
    }
  }, []);
  const l = Ke && s !== "denied", c = y.useRef(null), [d, u] = jn(!1, {
    value: o
  }), f = y.useRef(!1), h = () => {
    if (l && !c.current) {
      const p = new Ke();
      p.onstart = () => {
        u(!0);
      }, p.onend = () => {
        u(!1);
      }, p.onresult = (g) => {
        var E, _, T;
        if (!f.current) {
          const v = (T = (_ = (E = g.results) == null ? void 0 : E[0]) == null ? void 0 : _[0]) == null ? void 0 : T.transcript;
          n(v);
        }
        f.current = !1;
      }, c.current = p;
    }
  }, b = pe((p) => {
    p && !d || (f.current = p, i ? r == null || r(!d) : (h(), c.current && (d ? (c.current.stop(), r == null || r(!1)) : (c.current.start(), r == null || r(!0)))));
  });
  return [l, b, d];
}
function Ji(e, t, n) {
  return $o(e, t) || n;
}
const es = /* @__PURE__ */ y.forwardRef((e, t) => {
  const {
    prefixCls: n,
    styles: o = {},
    classNames: r = {},
    className: i,
    rootClassName: s,
    style: a,
    defaultValue: l,
    value: c,
    readOnly: d,
    submitType: u = "enter",
    onSubmit: f,
    loading: h,
    components: b,
    onCancel: p,
    onChange: g,
    actions: E,
    onKeyPress: _,
    onKeyDown: T,
    disabled: v,
    allowSpeech: R,
    prefix: S,
    header: P,
    onPaste: O,
    onPasteFile: L,
    ...B
  } = e, {
    direction: $,
    getPrefixCls: k
  } = Rt(), M = k("sender", n), I = y.useRef(null), j = y.useRef(null);
  $i(t, () => {
    var x, D;
    return {
      nativeElement: I.current,
      focus: (x = j.current) == null ? void 0 : x.focus,
      blur: (D = j.current) == null ? void 0 : D.blur
    };
  });
  const N = Eo("sender"), q = `${M}-input`, [Q, he, me] = Yi(M), U = J(M, N.className, i, s, he, me, {
    [`${M}-rtl`]: $ === "rtl",
    [`${M}-disabled`]: v
  }), ee = `${M}-actions-btn`, ae = `${M}-actions-list`, [H, te] = jn(l || "", {
    value: c
  }), ce = (x, D) => {
    te(x), g && g(x, D);
  }, [K, ge, ve] = Zi((x) => {
    ce(`${H} ${x}`);
  }, R), ye = Ji(b, ["input"], br.TextArea), ne = {
    ...Di(B, {
      attr: !0,
      aria: !0,
      data: !0
    }),
    ref: j
  }, le = () => {
    H && f && !h && f(H);
  }, ke = () => {
    ce("");
  }, _e = y.useRef(!1), re = () => {
    _e.current = !0;
  }, ut = () => {
    _e.current = !1;
  }, Le = (x) => {
    const D = x.key === "Enter" && !_e.current;
    switch (u) {
      case "enter":
        D && !x.shiftKey && (x.preventDefault(), le());
        break;
      case "shiftEnter":
        D && x.shiftKey && (x.preventDefault(), le());
        break;
    }
    _ && _(x);
  }, Te = (x) => {
    var Y;
    const D = (Y = x.clipboardData) == null ? void 0 : Y.files[0];
    D && L && (L(D), x.preventDefault()), O == null || O(x);
  }, Re = (x) => {
    var D, Y;
    x.target !== ((D = I.current) == null ? void 0 : D.querySelector(`.${q}`)) && x.preventDefault(), (Y = j.current) == null || Y.focus();
  };
  let V = /* @__PURE__ */ y.createElement(Sr, {
    className: `${ae}-presets`
  }, R && /* @__PURE__ */ y.createElement(Ki, null), h ? /* @__PURE__ */ y.createElement(En, null) : /* @__PURE__ */ y.createElement(Cn, null));
  return typeof E == "function" ? V = E(V, {
    components: {
      SendButton: Cn,
      ClearButton: Vi,
      LoadingButton: En
    }
  }) : E && (V = E), Q(/* @__PURE__ */ y.createElement("div", {
    ref: I,
    className: U,
    style: {
      ...N.style,
      ...a
    }
  }, P && /* @__PURE__ */ y.createElement(or.Provider, {
    value: {
      prefixCls: M
    }
  }, P), /* @__PURE__ */ y.createElement("div", {
    className: `${M}-content`,
    onMouseDown: Re
  }, S && /* @__PURE__ */ y.createElement("div", {
    className: J(`${M}-prefix`, N.classNames.prefix, r.prefix),
    style: {
      ...N.styles.prefix,
      ...o.prefix
    }
  }, S), /* @__PURE__ */ y.createElement(ye, se({}, ne, {
    disabled: v,
    style: {
      ...N.styles.input,
      ...o.input
    },
    className: J(q, N.classNames.input, r.input),
    autoSize: {
      maxRows: 8
    },
    value: H,
    onChange: (x) => {
      ce(x.target.value, x), ge(!0);
    },
    onPressEnter: Le,
    onCompositionStart: re,
    onCompositionEnd: ut,
    onKeyDown: T,
    onPaste: Te,
    variant: "borderless",
    readOnly: d
  })), /* @__PURE__ */ y.createElement("div", {
    className: J(ae, N.classNames.actions, r.actions),
    style: {
      ...N.styles.actions,
      ...o.actions
    }
  }, /* @__PURE__ */ y.createElement(ct.Provider, {
    value: {
      prefixCls: ee,
      onSend: le,
      onSendDisabled: !H,
      onClear: ke,
      onClearDisabled: !H,
      onCancel: p,
      onCancelDisabled: !h,
      onSpeech: () => ge(!1),
      onSpeechDisabled: !K,
      speechRecording: ve,
      disabled: v
    }
  }, V)))));
}), ir = es;
ir.Header = Ni;
function ts(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ns(e, t = !1) {
  try {
    if (gr(e))
      return e;
    if (t && !ts(e))
      return;
    if (typeof e == "string") {
      let n = e.trim();
      return n.startsWith(";") && (n = n.slice(1)), n.endsWith(";") && (n = n.slice(0, -1)), new Function(`return (...args) => (${n})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function rs(e, t) {
  return fr(() => ns(e, t), [e, t]);
}
function os({
  value: e,
  onValueChange: t
}) {
  const [n, o] = Rn(e), r = Z(t);
  r.current = t;
  const i = Z(n);
  return i.current = n, fe(() => {
    r.current(n);
  }, [n]), fe(() => {
    Vr(e, i.current) || o(e);
  }, [e]), [n, o];
}
function Tn(e, t) {
  return e ? /* @__PURE__ */ oe.jsx(Tt, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function is({
  key: e,
  slots: t,
  targets: n
}, o) {
  return t[e] ? (...r) => n ? n.map((i, s) => /* @__PURE__ */ oe.jsx(Vt, {
    params: r,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: Tn(i, {
      clone: !0,
      ...o
    })
  }, s)) : /* @__PURE__ */ oe.jsx(Vt, {
    params: r,
    forceClone: (o == null ? void 0 : o.forceClone) ?? !0,
    children: Tn(t[e], {
      clone: !0,
      ...o
    })
  }) : void 0;
}
const ls = ho(({
  slots: e,
  children: t,
  setSlotParams: n,
  onValueChange: o,
  onChange: r,
  onPasteFile: i,
  upload: s,
  elRef: a,
  ...l
}) => {
  const c = rs(l.actions, !0), [d, u] = os({
    onValueChange: o,
    value: l.value
  });
  return /* @__PURE__ */ oe.jsxs(oe.Fragment, {
    children: [/* @__PURE__ */ oe.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ oe.jsx(ir, {
      ...l,
      value: d,
      allowSpeech: !0,
      ref: a,
      onChange: (f) => {
        r == null || r(f), u(f);
      },
      onPasteFile: async (f) => {
        const h = await s(Array.isArray(f) ? f : [f]);
        i == null || i(h);
      },
      header: e.header ? /* @__PURE__ */ oe.jsx(Tt, {
        slot: e.header
      }) : l.header,
      prefix: e.prefix ? /* @__PURE__ */ oe.jsx(Tt, {
        slot: e.prefix
      }) : l.prefix,
      actions: e.actions ? is({
        slots: e,
        setSlotParams: n,
        key: "actions"
      }, {
        clone: !0
      }) : c || l.actions
    })]
  });
});
export {
  ls as Sender,
  ls as default
};
