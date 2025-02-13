import { i as lr, a as bt, r as cr, g as ur, w as je, c as oe, b as fr } from "./Index-DJpjn4M_.js";
const O = window.ms_globals.React, l = window.ms_globals.React, ir = window.ms_globals.React.isValidElement, pe = window.ms_globals.React.useRef, sr = window.ms_globals.React.useLayoutEffect, we = window.ms_globals.React.useEffect, xn = window.ms_globals.React.useMemo, ar = window.ms_globals.React.forwardRef, En = window.ms_globals.React.useState, jt = window.ms_globals.ReactDOM, Ne = window.ms_globals.ReactDOM.createPortal, dr = window.ms_globals.internalContext.useContextPropsContext, Dt = window.ms_globals.internalContext.ContextPropsProvider, pr = window.ms_globals.antd.ConfigProvider, Cn = window.ms_globals.antd.Upload, He = window.ms_globals.antd.theme, mr = window.ms_globals.antd.Progress, st = window.ms_globals.antd.Button, hr = window.ms_globals.antd.Flex, at = window.ms_globals.antd.Typography, gr = window.ms_globals.antdIcons.FileTextFilled, vr = window.ms_globals.antdIcons.CloseCircleFilled, br = window.ms_globals.antdIcons.FileExcelFilled, yr = window.ms_globals.antdIcons.FileImageFilled, Sr = window.ms_globals.antdIcons.FileMarkdownFilled, wr = window.ms_globals.antdIcons.FilePdfFilled, xr = window.ms_globals.antdIcons.FilePptFilled, Er = window.ms_globals.antdIcons.FileWordFilled, Cr = window.ms_globals.antdIcons.FileZipFilled, _r = window.ms_globals.antdIcons.PlusOutlined, Lr = window.ms_globals.antdIcons.LeftOutlined, Tr = window.ms_globals.antdIcons.RightOutlined, zt = window.ms_globals.antdCssinjs.unit, lt = window.ms_globals.antdCssinjs.token2CSSVar, Nt = window.ms_globals.antdCssinjs.useStyleRegister, Rr = window.ms_globals.antdCssinjs.useCSSVarRegister, Ir = window.ms_globals.antdCssinjs.createTheme, Mr = window.ms_globals.antdCssinjs.useCacheToken;
var Pr = /\s/;
function Or(e) {
  for (var t = e.length; t-- && Pr.test(e.charAt(t)); )
    ;
  return t;
}
var Fr = /^\s+/;
function Ar(e) {
  return e && e.slice(0, Or(e) + 1).replace(Fr, "");
}
var Ht = NaN, $r = /^[-+]0x[0-9a-f]+$/i, kr = /^0b[01]+$/i, jr = /^0o[0-7]+$/i, Dr = parseInt;
function Ut(e) {
  if (typeof e == "number")
    return e;
  if (lr(e))
    return Ht;
  if (bt(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = bt(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ar(e);
  var n = kr.test(e);
  return n || jr.test(e) ? Dr(e.slice(2), n ? 2 : 8) : $r.test(e) ? Ht : +e;
}
function zr() {
}
var ct = function() {
  return cr.Date.now();
}, Nr = "Expected a function", Hr = Math.max, Ur = Math.min;
function Br(e, t, n) {
  var r, o, i, s, a, c, u = 0, p = !1, f = !1, d = !0;
  if (typeof e != "function")
    throw new TypeError(Nr);
  t = Ut(t) || 0, bt(n) && (p = !!n.leading, f = "maxWait" in n, i = f ? Hr(Ut(n.maxWait) || 0, t) : i, d = "trailing" in n ? !!n.trailing : d);
  function h(v) {
    var y = r, w = o;
    return r = o = void 0, u = v, s = e.apply(w, y), s;
  }
  function b(v) {
    return u = v, a = setTimeout(C, t), p ? h(v) : s;
  }
  function g(v) {
    var y = v - c, w = v - u, P = t - y;
    return f ? Ur(P, i - w) : P;
  }
  function m(v) {
    var y = v - c, w = v - u;
    return c === void 0 || y >= t || y < 0 || f && w >= i;
  }
  function C() {
    var v = ct();
    if (m(v))
      return _(v);
    a = setTimeout(C, g(v));
  }
  function _(v) {
    return a = void 0, d && r ? h(v) : (r = o = void 0, s);
  }
  function x() {
    a !== void 0 && clearTimeout(a), u = 0, r = c = o = a = void 0;
  }
  function S() {
    return a === void 0 ? s : _(ct());
  }
  function E() {
    var v = ct(), y = m(v);
    if (r = arguments, o = this, c = v, y) {
      if (a === void 0)
        return b(c);
      if (f)
        return clearTimeout(a), a = setTimeout(C, t), h(c);
    }
    return a === void 0 && (a = setTimeout(C, t)), s;
  }
  return E.cancel = x, E.flush = S, E;
}
var _n = {
  exports: {}
}, Xe = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Xr = l, Vr = Symbol.for("react.element"), Wr = Symbol.for("react.fragment"), Gr = Object.prototype.hasOwnProperty, Kr = Xr.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, qr = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Ln(e, t, n) {
  var r, o = {}, i = null, s = null;
  n !== void 0 && (i = "" + n), t.key !== void 0 && (i = "" + t.key), t.ref !== void 0 && (s = t.ref);
  for (r in t) Gr.call(t, r) && !qr.hasOwnProperty(r) && (o[r] = t[r]);
  if (e && e.defaultProps) for (r in t = e.defaultProps, t) o[r] === void 0 && (o[r] = t[r]);
  return {
    $$typeof: Vr,
    type: e,
    key: i,
    ref: s,
    props: o,
    _owner: Kr.current
  };
}
Xe.Fragment = Wr;
Xe.jsx = Ln;
Xe.jsxs = Ln;
_n.exports = Xe;
var ge = _n.exports;
const {
  SvelteComponent: Zr,
  assign: Bt,
  binding_callbacks: Xt,
  check_outros: Qr,
  children: Tn,
  claim_element: Rn,
  claim_space: Yr,
  component_subscribe: Vt,
  compute_slots: Jr,
  create_slot: eo,
  detach: be,
  element: In,
  empty: Wt,
  exclude_internal_props: Gt,
  get_all_dirty_from_scope: to,
  get_slot_changes: no,
  group_outros: ro,
  init: oo,
  insert_hydration: De,
  safe_not_equal: io,
  set_custom_element_data: Mn,
  space: so,
  transition_in: ze,
  transition_out: yt,
  update_slot_base: ao
} = window.__gradio__svelte__internal, {
  beforeUpdate: lo,
  getContext: co,
  onDestroy: uo,
  setContext: fo
} = window.__gradio__svelte__internal;
function Kt(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[7].default
  ), o = eo(
    r,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = In("svelte-slot"), o && o.c(), this.h();
    },
    l(i) {
      t = Rn(i, "SVELTE-SLOT", {
        class: !0
      });
      var s = Tn(t);
      o && o.l(s), s.forEach(be), this.h();
    },
    h() {
      Mn(t, "class", "svelte-1rt0kpf");
    },
    m(i, s) {
      De(i, t, s), o && o.m(t, null), e[9](t), n = !0;
    },
    p(i, s) {
      o && o.p && (!n || s & /*$$scope*/
      64) && ao(
        o,
        r,
        i,
        /*$$scope*/
        i[6],
        n ? no(
          r,
          /*$$scope*/
          i[6],
          s,
          null
        ) : to(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      n || (ze(o, i), n = !0);
    },
    o(i) {
      yt(o, i), n = !1;
    },
    d(i) {
      i && be(t), o && o.d(i), e[9](null);
    }
  };
}
function po(e) {
  let t, n, r, o, i = (
    /*$$slots*/
    e[4].default && Kt(e)
  );
  return {
    c() {
      t = In("react-portal-target"), n = so(), i && i.c(), r = Wt(), this.h();
    },
    l(s) {
      t = Rn(s, "REACT-PORTAL-TARGET", {
        class: !0
      }), Tn(t).forEach(be), n = Yr(s), i && i.l(s), r = Wt(), this.h();
    },
    h() {
      Mn(t, "class", "svelte-1rt0kpf");
    },
    m(s, a) {
      De(s, t, a), e[8](t), De(s, n, a), i && i.m(s, a), De(s, r, a), o = !0;
    },
    p(s, [a]) {
      /*$$slots*/
      s[4].default ? i ? (i.p(s, a), a & /*$$slots*/
      16 && ze(i, 1)) : (i = Kt(s), i.c(), ze(i, 1), i.m(r.parentNode, r)) : i && (ro(), yt(i, 1, 1, () => {
        i = null;
      }), Qr());
    },
    i(s) {
      o || (ze(i), o = !0);
    },
    o(s) {
      yt(i), o = !1;
    },
    d(s) {
      s && (be(t), be(n), be(r)), e[8](null), i && i.d(s);
    }
  };
}
function qt(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function mo(e, t, n) {
  let r, o, {
    $$slots: i = {},
    $$scope: s
  } = t;
  const a = Jr(i);
  let {
    svelteInit: c
  } = t;
  const u = je(qt(t)), p = je();
  Vt(e, p, (S) => n(0, r = S));
  const f = je();
  Vt(e, f, (S) => n(1, o = S));
  const d = [], h = co("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: g,
    subSlotIndex: m
  } = ur() || {}, C = c({
    parent: h,
    props: u,
    target: p,
    slot: f,
    slotKey: b,
    slotIndex: g,
    subSlotIndex: m,
    onDestroy(S) {
      d.push(S);
    }
  });
  fo("$$ms-gr-react-wrapper", C), lo(() => {
    u.set(qt(t));
  }), uo(() => {
    d.forEach((S) => S());
  });
  function _(S) {
    Xt[S ? "unshift" : "push"](() => {
      r = S, p.set(r);
    });
  }
  function x(S) {
    Xt[S ? "unshift" : "push"](() => {
      o = S, f.set(o);
    });
  }
  return e.$$set = (S) => {
    n(17, t = Bt(Bt({}, t), Gt(S))), "svelteInit" in S && n(5, c = S.svelteInit), "$$scope" in S && n(6, s = S.$$scope);
  }, t = Gt(t), [r, o, p, f, a, c, s, i, _, x];
}
class ho extends Zr {
  constructor(t) {
    super(), oo(this, t, mo, po, io, {
      svelteInit: 5
    });
  }
}
const Zt = window.ms_globals.rerender, ut = window.ms_globals.tree;
function go(e, t = {}) {
  function n(r) {
    const o = je(), i = new ho({
      ...r,
      props: {
        svelteInit(s) {
          window.ms_globals.autokey += 1;
          const a = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: s.props,
            slot: s.slot,
            target: s.target,
            slotIndex: s.slotIndex,
            subSlotIndex: s.subSlotIndex,
            ignore: t.ignore,
            slotKey: s.slotKey,
            nodes: []
          }, c = s.parent ?? ut;
          return c.nodes = [...c.nodes, a], Zt({
            createPortal: Ne,
            node: ut
          }), s.onDestroy(() => {
            c.nodes = c.nodes.filter((u) => u.svelteInstance !== o), Zt({
              createPortal: Ne,
              node: ut
            });
          }), a;
        },
        ...r.props
      }
    });
    return o.set(i), i;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(n);
    });
  });
}
const vo = "1.0.5", bo = /* @__PURE__ */ l.createContext({}), yo = {
  classNames: {},
  styles: {},
  className: "",
  style: {}
}, So = (e) => {
  const t = l.useContext(bo);
  return l.useMemo(() => ({
    ...yo,
    ...t[e]
  }), [t[e]]);
};
function Le() {
  return Le = Object.assign ? Object.assign.bind() : function(e) {
    for (var t = 1; t < arguments.length; t++) {
      var n = arguments[t];
      for (var r in n) ({}).hasOwnProperty.call(n, r) && (e[r] = n[r]);
    }
    return e;
  }, Le.apply(null, arguments);
}
function Ue() {
  const {
    getPrefixCls: e,
    direction: t,
    csp: n,
    iconPrefixCls: r,
    theme: o
  } = l.useContext(pr.ConfigContext);
  return {
    theme: o,
    getPrefixCls: e,
    direction: t,
    csp: n,
    iconPrefixCls: r
  };
}
function xe(e) {
  var t = O.useRef();
  t.current = e;
  var n = O.useCallback(function() {
    for (var r, o = arguments.length, i = new Array(o), s = 0; s < o; s++)
      i[s] = arguments[s];
    return (r = t.current) === null || r === void 0 ? void 0 : r.call.apply(r, [t].concat(i));
  }, []);
  return n;
}
function wo(e) {
  if (Array.isArray(e)) return e;
}
function xo(e, t) {
  var n = e == null ? null : typeof Symbol < "u" && e[Symbol.iterator] || e["@@iterator"];
  if (n != null) {
    var r, o, i, s, a = [], c = !0, u = !1;
    try {
      if (i = (n = n.call(e)).next, t === 0) {
        if (Object(n) !== n) return;
        c = !1;
      } else for (; !(c = (r = i.call(n)).done) && (a.push(r.value), a.length !== t); c = !0) ;
    } catch (p) {
      u = !0, o = p;
    } finally {
      try {
        if (!c && n.return != null && (s = n.return(), Object(s) !== s)) return;
      } finally {
        if (u) throw o;
      }
    }
    return a;
  }
}
function Qt(e, t) {
  (t == null || t > e.length) && (t = e.length);
  for (var n = 0, r = Array(t); n < t; n++) r[n] = e[n];
  return r;
}
function Eo(e, t) {
  if (e) {
    if (typeof e == "string") return Qt(e, t);
    var n = {}.toString.call(e).slice(8, -1);
    return n === "Object" && e.constructor && (n = e.constructor.name), n === "Map" || n === "Set" ? Array.from(e) : n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? Qt(e, t) : void 0;
  }
}
function Co() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function Z(e, t) {
  return wo(e) || xo(e, t) || Eo(e, t) || Co();
}
function Ve() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
var Yt = Ve() ? O.useLayoutEffect : O.useEffect, _o = function(t, n) {
  var r = O.useRef(!0);
  Yt(function() {
    return t(r.current);
  }, n), Yt(function() {
    return r.current = !1, function() {
      r.current = !0;
    };
  }, []);
}, Jt = function(t, n) {
  _o(function(r) {
    if (!r)
      return t();
  }, n);
};
function Te(e) {
  var t = O.useRef(!1), n = O.useState(e), r = Z(n, 2), o = r[0], i = r[1];
  O.useEffect(function() {
    return t.current = !1, function() {
      t.current = !0;
    };
  }, []);
  function s(a, c) {
    c && t.current || i(a);
  }
  return [o, s];
}
function ft(e) {
  return e !== void 0;
}
function Lo(e, t) {
  var n = t || {}, r = n.defaultValue, o = n.value, i = n.onChange, s = n.postState, a = Te(function() {
    return ft(o) ? o : ft(r) ? typeof r == "function" ? r() : r : typeof e == "function" ? e() : e;
  }), c = Z(a, 2), u = c[0], p = c[1], f = o !== void 0 ? o : u, d = s ? s(f) : f, h = xe(i), b = Te([f]), g = Z(b, 2), m = g[0], C = g[1];
  Jt(function() {
    var x = m[0];
    u !== x && h(u, x);
  }, [m]), Jt(function() {
    ft(o) || p(o);
  }, [o]);
  var _ = xe(function(x, S) {
    p(x, S), C([f], S);
  });
  return [d, _];
}
function K(e) {
  "@babel/helpers - typeof";
  return K = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(t) {
    return typeof t;
  } : function(t) {
    return t && typeof Symbol == "function" && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t;
  }, K(e);
}
var Pn = {
  exports: {}
}, F = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Mt = Symbol.for("react.element"), Pt = Symbol.for("react.portal"), We = Symbol.for("react.fragment"), Ge = Symbol.for("react.strict_mode"), Ke = Symbol.for("react.profiler"), qe = Symbol.for("react.provider"), Ze = Symbol.for("react.context"), To = Symbol.for("react.server_context"), Qe = Symbol.for("react.forward_ref"), Ye = Symbol.for("react.suspense"), Je = Symbol.for("react.suspense_list"), et = Symbol.for("react.memo"), tt = Symbol.for("react.lazy"), Ro = Symbol.for("react.offscreen"), On;
On = Symbol.for("react.module.reference");
function ie(e) {
  if (typeof e == "object" && e !== null) {
    var t = e.$$typeof;
    switch (t) {
      case Mt:
        switch (e = e.type, e) {
          case We:
          case Ke:
          case Ge:
          case Ye:
          case Je:
            return e;
          default:
            switch (e = e && e.$$typeof, e) {
              case To:
              case Ze:
              case Qe:
              case tt:
              case et:
              case qe:
                return e;
              default:
                return t;
            }
        }
      case Pt:
        return t;
    }
  }
}
F.ContextConsumer = Ze;
F.ContextProvider = qe;
F.Element = Mt;
F.ForwardRef = Qe;
F.Fragment = We;
F.Lazy = tt;
F.Memo = et;
F.Portal = Pt;
F.Profiler = Ke;
F.StrictMode = Ge;
F.Suspense = Ye;
F.SuspenseList = Je;
F.isAsyncMode = function() {
  return !1;
};
F.isConcurrentMode = function() {
  return !1;
};
F.isContextConsumer = function(e) {
  return ie(e) === Ze;
};
F.isContextProvider = function(e) {
  return ie(e) === qe;
};
F.isElement = function(e) {
  return typeof e == "object" && e !== null && e.$$typeof === Mt;
};
F.isForwardRef = function(e) {
  return ie(e) === Qe;
};
F.isFragment = function(e) {
  return ie(e) === We;
};
F.isLazy = function(e) {
  return ie(e) === tt;
};
F.isMemo = function(e) {
  return ie(e) === et;
};
F.isPortal = function(e) {
  return ie(e) === Pt;
};
F.isProfiler = function(e) {
  return ie(e) === Ke;
};
F.isStrictMode = function(e) {
  return ie(e) === Ge;
};
F.isSuspense = function(e) {
  return ie(e) === Ye;
};
F.isSuspenseList = function(e) {
  return ie(e) === Je;
};
F.isValidElementType = function(e) {
  return typeof e == "string" || typeof e == "function" || e === We || e === Ke || e === Ge || e === Ye || e === Je || e === Ro || typeof e == "object" && e !== null && (e.$$typeof === tt || e.$$typeof === et || e.$$typeof === qe || e.$$typeof === Ze || e.$$typeof === Qe || e.$$typeof === On || e.getModuleId !== void 0);
};
F.typeOf = ie;
Pn.exports = F;
var dt = Pn.exports, Io = Symbol.for("react.element"), Mo = Symbol.for("react.transitional.element"), Po = Symbol.for("react.fragment");
function Oo(e) {
  return (
    // Base object type
    e && K(e) === "object" && // React Element type
    (e.$$typeof === Io || e.$$typeof === Mo) && // React Fragment type
    e.type === Po
  );
}
var Fo = function(t, n) {
  typeof t == "function" ? t(n) : K(t) === "object" && t && "current" in t && (t.current = n);
}, Ao = function(t) {
  var n, r;
  if (!t)
    return !1;
  if (Fn(t) && t.props.propertyIsEnumerable("ref"))
    return !0;
  var o = dt.isMemo(t) ? t.type.type : t.type;
  return !(typeof o == "function" && !((n = o.prototype) !== null && n !== void 0 && n.render) && o.$$typeof !== dt.ForwardRef || typeof t == "function" && !((r = t.prototype) !== null && r !== void 0 && r.render) && t.$$typeof !== dt.ForwardRef);
};
function Fn(e) {
  return /* @__PURE__ */ ir(e) && !Oo(e);
}
var $o = function(t) {
  if (t && Fn(t)) {
    var n = t;
    return n.props.propertyIsEnumerable("ref") ? n.props.ref : n.ref;
  }
  return null;
};
function ko(e, t) {
  if (K(e) != "object" || !e) return e;
  var n = e[Symbol.toPrimitive];
  if (n !== void 0) {
    var r = n.call(e, t || "default");
    if (K(r) != "object") return r;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (t === "string" ? String : Number)(e);
}
function An(e) {
  var t = ko(e, "string");
  return K(t) == "symbol" ? t : t + "";
}
function T(e, t, n) {
  return (t = An(t)) in e ? Object.defineProperty(e, t, {
    value: n,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : e[t] = n, e;
}
function en(e, t) {
  var n = Object.keys(e);
  if (Object.getOwnPropertySymbols) {
    var r = Object.getOwnPropertySymbols(e);
    t && (r = r.filter(function(o) {
      return Object.getOwnPropertyDescriptor(e, o).enumerable;
    })), n.push.apply(n, r);
  }
  return n;
}
function L(e) {
  for (var t = 1; t < arguments.length; t++) {
    var n = arguments[t] != null ? arguments[t] : {};
    t % 2 ? en(Object(n), !0).forEach(function(r) {
      T(e, r, n[r]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : en(Object(n)).forEach(function(r) {
      Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(n, r));
    });
  }
  return e;
}
const Re = /* @__PURE__ */ l.createContext(null);
function tn(e) {
  const {
    getDropContainer: t,
    className: n,
    prefixCls: r,
    children: o
  } = e, {
    disabled: i
  } = l.useContext(Re), [s, a] = l.useState(), [c, u] = l.useState(null);
  if (l.useEffect(() => {
    const d = t == null ? void 0 : t();
    s !== d && a(d);
  }, [t]), l.useEffect(() => {
    if (s) {
      const d = () => {
        u(!0);
      }, h = (m) => {
        m.preventDefault();
      }, b = (m) => {
        m.relatedTarget || u(!1);
      }, g = (m) => {
        u(!1), m.preventDefault();
      };
      return document.addEventListener("dragenter", d), document.addEventListener("dragover", h), document.addEventListener("dragleave", b), document.addEventListener("drop", g), () => {
        document.removeEventListener("dragenter", d), document.removeEventListener("dragover", h), document.removeEventListener("dragleave", b), document.removeEventListener("drop", g);
      };
    }
  }, [!!s]), !(t && s && !i))
    return null;
  const f = `${r}-drop-area`;
  return /* @__PURE__ */ Ne(/* @__PURE__ */ l.createElement("div", {
    className: oe(f, n, {
      [`${f}-on-body`]: s.tagName === "BODY"
    }),
    style: {
      display: c ? "block" : "none"
    }
  }, o), s);
}
function nn(e) {
  return e instanceof HTMLElement || e instanceof SVGElement;
}
function jo(e) {
  return e && K(e) === "object" && nn(e.nativeElement) ? e.nativeElement : nn(e) ? e : null;
}
function Do(e) {
  var t = jo(e);
  if (t)
    return t;
  if (e instanceof l.Component) {
    var n;
    return (n = jt.findDOMNode) === null || n === void 0 ? void 0 : n.call(jt, e);
  }
  return null;
}
function zo(e, t) {
  if (e == null) return {};
  var n = {};
  for (var r in e) if ({}.hasOwnProperty.call(e, r)) {
    if (t.includes(r)) continue;
    n[r] = e[r];
  }
  return n;
}
function rn(e, t) {
  if (e == null) return {};
  var n, r, o = zo(e, t);
  if (Object.getOwnPropertySymbols) {
    var i = Object.getOwnPropertySymbols(e);
    for (r = 0; r < i.length; r++) n = i[r], t.includes(n) || {}.propertyIsEnumerable.call(e, n) && (o[n] = e[n]);
  }
  return o;
}
var No = /* @__PURE__ */ O.createContext({});
function Ee(e, t) {
  if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function on(e, t) {
  for (var n = 0; n < t.length; n++) {
    var r = t[n];
    r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), Object.defineProperty(e, An(r.key), r);
  }
}
function Ce(e, t, n) {
  return t && on(e.prototype, t), n && on(e, n), Object.defineProperty(e, "prototype", {
    writable: !1
  }), e;
}
function St(e, t) {
  return St = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(n, r) {
    return n.__proto__ = r, n;
  }, St(e, t);
}
function nt(e, t) {
  if (typeof t != "function" && t !== null) throw new TypeError("Super expression must either be null or a function");
  e.prototype = Object.create(t && t.prototype, {
    constructor: {
      value: e,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(e, "prototype", {
    writable: !1
  }), t && St(e, t);
}
function Be(e) {
  return Be = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
    return t.__proto__ || Object.getPrototypeOf(t);
  }, Be(e);
}
function $n() {
  try {
    var e = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return ($n = function() {
    return !!e;
  })();
}
function ve(e) {
  if (e === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return e;
}
function Ho(e, t) {
  if (t && (K(t) == "object" || typeof t == "function")) return t;
  if (t !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return ve(e);
}
function rt(e) {
  var t = $n();
  return function() {
    var n, r = Be(e);
    if (t) {
      var o = Be(this).constructor;
      n = Reflect.construct(r, arguments, o);
    } else n = r.apply(this, arguments);
    return Ho(this, n);
  };
}
var Uo = /* @__PURE__ */ function(e) {
  nt(n, e);
  var t = rt(n);
  function n() {
    return Ee(this, n), t.apply(this, arguments);
  }
  return Ce(n, [{
    key: "render",
    value: function() {
      return this.props.children;
    }
  }]), n;
}(O.Component);
function Bo(e) {
  var t = O.useReducer(function(a) {
    return a + 1;
  }, 0), n = Z(t, 2), r = n[1], o = O.useRef(e), i = xe(function() {
    return o.current;
  }), s = xe(function(a) {
    o.current = typeof a == "function" ? a(o.current) : a, r();
  });
  return [i, s];
}
var me = "none", Pe = "appear", Oe = "enter", Fe = "leave", sn = "none", le = "prepare", ye = "start", Se = "active", Ot = "end", kn = "prepared";
function an(e, t) {
  var n = {};
  return n[e.toLowerCase()] = t.toLowerCase(), n["Webkit".concat(e)] = "webkit".concat(t), n["Moz".concat(e)] = "moz".concat(t), n["ms".concat(e)] = "MS".concat(t), n["O".concat(e)] = "o".concat(t.toLowerCase()), n;
}
function Xo(e, t) {
  var n = {
    animationend: an("Animation", "AnimationEnd"),
    transitionend: an("Transition", "TransitionEnd")
  };
  return e && ("AnimationEvent" in t || delete n.animationend.animation, "TransitionEvent" in t || delete n.transitionend.transition), n;
}
var Vo = Xo(Ve(), typeof window < "u" ? window : {}), jn = {};
if (Ve()) {
  var Wo = document.createElement("div");
  jn = Wo.style;
}
var Ae = {};
function Dn(e) {
  if (Ae[e])
    return Ae[e];
  var t = Vo[e];
  if (t)
    for (var n = Object.keys(t), r = n.length, o = 0; o < r; o += 1) {
      var i = n[o];
      if (Object.prototype.hasOwnProperty.call(t, i) && i in jn)
        return Ae[e] = t[i], Ae[e];
    }
  return "";
}
var zn = Dn("animationend"), Nn = Dn("transitionend"), Hn = !!(zn && Nn), ln = zn || "animationend", cn = Nn || "transitionend";
function un(e, t) {
  if (!e) return null;
  if (K(e) === "object") {
    var n = t.replace(/-\w/g, function(r) {
      return r[1].toUpperCase();
    });
    return e[n];
  }
  return "".concat(e, "-").concat(t);
}
const Go = function(e) {
  var t = pe();
  function n(o) {
    o && (o.removeEventListener(cn, e), o.removeEventListener(ln, e));
  }
  function r(o) {
    t.current && t.current !== o && n(t.current), o && o !== t.current && (o.addEventListener(cn, e), o.addEventListener(ln, e), t.current = o);
  }
  return O.useEffect(function() {
    return function() {
      n(t.current);
    };
  }, []), [r, n];
};
var Un = Ve() ? sr : we, Bn = function(t) {
  return +setTimeout(t, 16);
}, Xn = function(t) {
  return clearTimeout(t);
};
typeof window < "u" && "requestAnimationFrame" in window && (Bn = function(t) {
  return window.requestAnimationFrame(t);
}, Xn = function(t) {
  return window.cancelAnimationFrame(t);
});
var fn = 0, Ft = /* @__PURE__ */ new Map();
function Vn(e) {
  Ft.delete(e);
}
var wt = function(t) {
  var n = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 1;
  fn += 1;
  var r = fn;
  function o(i) {
    if (i === 0)
      Vn(r), t();
    else {
      var s = Bn(function() {
        o(i - 1);
      });
      Ft.set(r, s);
    }
  }
  return o(n), r;
};
wt.cancel = function(e) {
  var t = Ft.get(e);
  return Vn(e), Xn(t);
};
const Ko = function() {
  var e = O.useRef(null);
  function t() {
    wt.cancel(e.current);
  }
  function n(r) {
    var o = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 2;
    t();
    var i = wt(function() {
      o <= 1 ? r({
        isCanceled: function() {
          return i !== e.current;
        }
      }) : n(r, o - 1);
    });
    e.current = i;
  }
  return O.useEffect(function() {
    return function() {
      t();
    };
  }, []), [n, t];
};
var qo = [le, ye, Se, Ot], Zo = [le, kn], Wn = !1, Qo = !0;
function Gn(e) {
  return e === Se || e === Ot;
}
const Yo = function(e, t, n) {
  var r = Te(sn), o = Z(r, 2), i = o[0], s = o[1], a = Ko(), c = Z(a, 2), u = c[0], p = c[1];
  function f() {
    s(le, !0);
  }
  var d = t ? Zo : qo;
  return Un(function() {
    if (i !== sn && i !== Ot) {
      var h = d.indexOf(i), b = d[h + 1], g = n(i);
      g === Wn ? s(b, !0) : b && u(function(m) {
        function C() {
          m.isCanceled() || s(b, !0);
        }
        g === !0 ? C() : Promise.resolve(g).then(C);
      });
    }
  }, [e, i]), O.useEffect(function() {
    return function() {
      p();
    };
  }, []), [f, i];
};
function Jo(e, t, n, r) {
  var o = r.motionEnter, i = o === void 0 ? !0 : o, s = r.motionAppear, a = s === void 0 ? !0 : s, c = r.motionLeave, u = c === void 0 ? !0 : c, p = r.motionDeadline, f = r.motionLeaveImmediately, d = r.onAppearPrepare, h = r.onEnterPrepare, b = r.onLeavePrepare, g = r.onAppearStart, m = r.onEnterStart, C = r.onLeaveStart, _ = r.onAppearActive, x = r.onEnterActive, S = r.onLeaveActive, E = r.onAppearEnd, v = r.onEnterEnd, y = r.onLeaveEnd, w = r.onVisibleChanged, P = Te(), $ = Z(P, 2), k = $[0], R = $[1], M = Bo(me), A = Z(M, 2), I = A[0], j = A[1], ee = Te(null), Y = Z(ee, 2), ce = Y[0], B = Y[1], D = I(), N = pe(!1), X = pe(null);
  function W() {
    return n();
  }
  var ne = pe(!1);
  function z() {
    j(me), B(null, !0);
  }
  var V = xe(function(J) {
    var q = I();
    if (q !== me) {
      var ue = W();
      if (!(J && !J.deadline && J.target !== ue)) {
        var Ie = ne.current, Me;
        q === Pe && Ie ? Me = E == null ? void 0 : E(ue, J) : q === Oe && Ie ? Me = v == null ? void 0 : v(ue, J) : q === Fe && Ie && (Me = y == null ? void 0 : y(ue, J)), Ie && Me !== !1 && z();
      }
    }
  }), Q = Go(V), H = Z(Q, 1), re = H[0], se = function(q) {
    switch (q) {
      case Pe:
        return T(T(T({}, le, d), ye, g), Se, _);
      case Oe:
        return T(T(T({}, le, h), ye, m), Se, x);
      case Fe:
        return T(T(T({}, le, b), ye, C), Se, S);
      default:
        return {};
    }
  }, U = O.useMemo(function() {
    return se(D);
  }, [D]), ae = Yo(D, !e, function(J) {
    if (J === le) {
      var q = U[le];
      return q ? q(W()) : Wn;
    }
    if (he in U) {
      var ue;
      B(((ue = U[he]) === null || ue === void 0 ? void 0 : ue.call(U, W(), null)) || null);
    }
    return he === Se && D !== me && (re(W()), p > 0 && (clearTimeout(X.current), X.current = setTimeout(function() {
      V({
        deadline: !0
      });
    }, p))), he === kn && z(), Qo;
  }), $t = Z(ae, 2), rr = $t[0], he = $t[1], or = Gn(he);
  ne.current = or;
  var kt = pe(null);
  Un(function() {
    if (!(N.current && kt.current === t)) {
      R(t);
      var J = N.current;
      N.current = !0;
      var q;
      !J && t && a && (q = Pe), J && t && i && (q = Oe), (J && !t && u || !J && f && !t && u) && (q = Fe);
      var ue = se(q);
      q && (e || ue[le]) ? (j(q), rr()) : j(me), kt.current = t;
    }
  }, [t]), we(function() {
    // Cancel appear
    (D === Pe && !a || // Cancel enter
    D === Oe && !i || // Cancel leave
    D === Fe && !u) && j(me);
  }, [a, i, u]), we(function() {
    return function() {
      N.current = !1, clearTimeout(X.current);
    };
  }, []);
  var ot = O.useRef(!1);
  we(function() {
    k && (ot.current = !0), k !== void 0 && D === me && ((ot.current || k) && (w == null || w(k)), ot.current = !0);
  }, [k, D]);
  var it = ce;
  return U[le] && he === ye && (it = L({
    transition: "none"
  }, it)), [D, he, it, k ?? t];
}
function ei(e) {
  var t = e;
  K(e) === "object" && (t = e.transitionSupport);
  function n(o, i) {
    return !!(o.motionName && t && i !== !1);
  }
  var r = /* @__PURE__ */ O.forwardRef(function(o, i) {
    var s = o.visible, a = s === void 0 ? !0 : s, c = o.removeOnLeave, u = c === void 0 ? !0 : c, p = o.forceRender, f = o.children, d = o.motionName, h = o.leavedClassName, b = o.eventProps, g = O.useContext(No), m = g.motion, C = n(o, m), _ = pe(), x = pe();
    function S() {
      try {
        return _.current instanceof HTMLElement ? _.current : Do(x.current);
      } catch {
        return null;
      }
    }
    var E = Jo(C, a, S, o), v = Z(E, 4), y = v[0], w = v[1], P = v[2], $ = v[3], k = O.useRef($);
    $ && (k.current = !0);
    var R = O.useCallback(function(Y) {
      _.current = Y, Fo(i, Y);
    }, [i]), M, A = L(L({}, b), {}, {
      visible: a
    });
    if (!f)
      M = null;
    else if (y === me)
      $ ? M = f(L({}, A), R) : !u && k.current && h ? M = f(L(L({}, A), {}, {
        className: h
      }), R) : p || !u && !h ? M = f(L(L({}, A), {}, {
        style: {
          display: "none"
        }
      }), R) : M = null;
    else {
      var I;
      w === le ? I = "prepare" : Gn(w) ? I = "active" : w === ye && (I = "start");
      var j = un(d, "".concat(y, "-").concat(I));
      M = f(L(L({}, A), {}, {
        className: oe(un(d, y), T(T({}, j, j && I), d, typeof d == "string")),
        style: P
      }), R);
    }
    if (/* @__PURE__ */ O.isValidElement(M) && Ao(M)) {
      var ee = $o(M);
      ee || (M = /* @__PURE__ */ O.cloneElement(M, {
        ref: R
      }));
    }
    return /* @__PURE__ */ O.createElement(Uo, {
      ref: x
    }, M);
  });
  return r.displayName = "CSSMotion", r;
}
const ti = ei(Hn);
var xt = "add", Et = "keep", Ct = "remove", pt = "removed";
function ni(e) {
  var t;
  return e && K(e) === "object" && "key" in e ? t = e : t = {
    key: e
  }, L(L({}, t), {}, {
    key: String(t.key)
  });
}
function _t() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [];
  return e.map(ni);
}
function ri() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [], t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : [], n = [], r = 0, o = t.length, i = _t(e), s = _t(t);
  i.forEach(function(u) {
    for (var p = !1, f = r; f < o; f += 1) {
      var d = s[f];
      if (d.key === u.key) {
        r < f && (n = n.concat(s.slice(r, f).map(function(h) {
          return L(L({}, h), {}, {
            status: xt
          });
        })), r = f), n.push(L(L({}, d), {}, {
          status: Et
        })), r += 1, p = !0;
        break;
      }
    }
    p || n.push(L(L({}, u), {}, {
      status: Ct
    }));
  }), r < o && (n = n.concat(s.slice(r).map(function(u) {
    return L(L({}, u), {}, {
      status: xt
    });
  })));
  var a = {};
  n.forEach(function(u) {
    var p = u.key;
    a[p] = (a[p] || 0) + 1;
  });
  var c = Object.keys(a).filter(function(u) {
    return a[u] > 1;
  });
  return c.forEach(function(u) {
    n = n.filter(function(p) {
      var f = p.key, d = p.status;
      return f !== u || d !== Ct;
    }), n.forEach(function(p) {
      p.key === u && (p.status = Et);
    });
  }), n;
}
var oi = ["component", "children", "onVisibleChanged", "onAllRemoved"], ii = ["status"], si = ["eventProps", "visible", "children", "motionName", "motionAppear", "motionEnter", "motionLeave", "motionLeaveImmediately", "motionDeadline", "removeOnLeave", "leavedClassName", "onAppearPrepare", "onAppearStart", "onAppearActive", "onAppearEnd", "onEnterStart", "onEnterActive", "onEnterEnd", "onLeaveStart", "onLeaveActive", "onLeaveEnd"];
function ai(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : ti, n = /* @__PURE__ */ function(r) {
    nt(i, r);
    var o = rt(i);
    function i() {
      var s;
      Ee(this, i);
      for (var a = arguments.length, c = new Array(a), u = 0; u < a; u++)
        c[u] = arguments[u];
      return s = o.call.apply(o, [this].concat(c)), T(ve(s), "state", {
        keyEntities: []
      }), T(ve(s), "removeKey", function(p) {
        s.setState(function(f) {
          var d = f.keyEntities.map(function(h) {
            return h.key !== p ? h : L(L({}, h), {}, {
              status: pt
            });
          });
          return {
            keyEntities: d
          };
        }, function() {
          var f = s.state.keyEntities, d = f.filter(function(h) {
            var b = h.status;
            return b !== pt;
          }).length;
          d === 0 && s.props.onAllRemoved && s.props.onAllRemoved();
        });
      }), s;
    }
    return Ce(i, [{
      key: "render",
      value: function() {
        var a = this, c = this.state.keyEntities, u = this.props, p = u.component, f = u.children, d = u.onVisibleChanged;
        u.onAllRemoved;
        var h = rn(u, oi), b = p || O.Fragment, g = {};
        return si.forEach(function(m) {
          g[m] = h[m], delete h[m];
        }), delete h.keys, /* @__PURE__ */ O.createElement(b, h, c.map(function(m, C) {
          var _ = m.status, x = rn(m, ii), S = _ === xt || _ === Et;
          return /* @__PURE__ */ O.createElement(t, Le({}, g, {
            key: x.key,
            visible: S,
            eventProps: x,
            onVisibleChanged: function(v) {
              d == null || d(v, {
                key: x.key
              }), v || a.removeKey(x.key);
            }
          }), function(E, v) {
            return f(L(L({}, E), {}, {
              index: C
            }), v);
          });
        }));
      }
    }], [{
      key: "getDerivedStateFromProps",
      value: function(a, c) {
        var u = a.keys, p = c.keyEntities, f = _t(u), d = ri(p, f);
        return {
          keyEntities: d.filter(function(h) {
            var b = p.find(function(g) {
              var m = g.key;
              return h.key === m;
            });
            return !(b && b.status === pt && h.status === Ct);
          })
        };
      }
    }]), i;
  }(O.Component);
  return T(n, "defaultProps", {
    component: "div"
  }), n;
}
const li = ai(Hn);
function ci(e, t) {
  const {
    children: n,
    upload: r,
    rootClassName: o
  } = e, i = l.useRef(null);
  return l.useImperativeHandle(t, () => i.current), /* @__PURE__ */ l.createElement(Cn, Le({}, r, {
    showUploadList: !1,
    rootClassName: o,
    ref: i
  }), n);
}
const Kn = /* @__PURE__ */ l.forwardRef(ci);
var qn = /* @__PURE__ */ Ce(function e() {
  Ee(this, e);
}), Zn = "CALC_UNIT", ui = new RegExp(Zn, "g");
function mt(e) {
  return typeof e == "number" ? "".concat(e).concat(Zn) : e;
}
var fi = /* @__PURE__ */ function(e) {
  nt(n, e);
  var t = rt(n);
  function n(r, o) {
    var i;
    Ee(this, n), i = t.call(this), T(ve(i), "result", ""), T(ve(i), "unitlessCssVar", void 0), T(ve(i), "lowPriority", void 0);
    var s = K(r);
    return i.unitlessCssVar = o, r instanceof n ? i.result = "(".concat(r.result, ")") : s === "number" ? i.result = mt(r) : s === "string" && (i.result = r), i;
  }
  return Ce(n, [{
    key: "add",
    value: function(o) {
      return o instanceof n ? this.result = "".concat(this.result, " + ").concat(o.getResult()) : (typeof o == "number" || typeof o == "string") && (this.result = "".concat(this.result, " + ").concat(mt(o))), this.lowPriority = !0, this;
    }
  }, {
    key: "sub",
    value: function(o) {
      return o instanceof n ? this.result = "".concat(this.result, " - ").concat(o.getResult()) : (typeof o == "number" || typeof o == "string") && (this.result = "".concat(this.result, " - ").concat(mt(o))), this.lowPriority = !0, this;
    }
  }, {
    key: "mul",
    value: function(o) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), o instanceof n ? this.result = "".concat(this.result, " * ").concat(o.getResult(!0)) : (typeof o == "number" || typeof o == "string") && (this.result = "".concat(this.result, " * ").concat(o)), this.lowPriority = !1, this;
    }
  }, {
    key: "div",
    value: function(o) {
      return this.lowPriority && (this.result = "(".concat(this.result, ")")), o instanceof n ? this.result = "".concat(this.result, " / ").concat(o.getResult(!0)) : (typeof o == "number" || typeof o == "string") && (this.result = "".concat(this.result, " / ").concat(o)), this.lowPriority = !1, this;
    }
  }, {
    key: "getResult",
    value: function(o) {
      return this.lowPriority || o ? "(".concat(this.result, ")") : this.result;
    }
  }, {
    key: "equal",
    value: function(o) {
      var i = this, s = o || {}, a = s.unit, c = !0;
      return typeof a == "boolean" ? c = a : Array.from(this.unitlessCssVar).some(function(u) {
        return i.result.includes(u);
      }) && (c = !1), this.result = this.result.replace(ui, c ? "px" : ""), typeof this.lowPriority < "u" ? "calc(".concat(this.result, ")") : this.result;
    }
  }]), n;
}(qn), di = /* @__PURE__ */ function(e) {
  nt(n, e);
  var t = rt(n);
  function n(r) {
    var o;
    return Ee(this, n), o = t.call(this), T(ve(o), "result", 0), r instanceof n ? o.result = r.result : typeof r == "number" && (o.result = r), o;
  }
  return Ce(n, [{
    key: "add",
    value: function(o) {
      return o instanceof n ? this.result += o.result : typeof o == "number" && (this.result += o), this;
    }
  }, {
    key: "sub",
    value: function(o) {
      return o instanceof n ? this.result -= o.result : typeof o == "number" && (this.result -= o), this;
    }
  }, {
    key: "mul",
    value: function(o) {
      return o instanceof n ? this.result *= o.result : typeof o == "number" && (this.result *= o), this;
    }
  }, {
    key: "div",
    value: function(o) {
      return o instanceof n ? this.result /= o.result : typeof o == "number" && (this.result /= o), this;
    }
  }, {
    key: "equal",
    value: function() {
      return this.result;
    }
  }]), n;
}(qn), pi = function(t, n) {
  var r = t === "css" ? fi : di;
  return function(o) {
    return new r(o, n);
  };
}, dn = function(t, n) {
  return "".concat([n, t.replace(/([A-Z]+)([A-Z][a-z]+)/g, "$1-$2").replace(/([a-z])([A-Z])/g, "$1-$2")].filter(Boolean).join("-"));
};
function pn(e, t, n, r) {
  var o = L({}, t[e]);
  if (r != null && r.deprecatedTokens) {
    var i = r.deprecatedTokens;
    i.forEach(function(a) {
      var c = Z(a, 2), u = c[0], p = c[1];
      if (o != null && o[u] || o != null && o[p]) {
        var f;
        (f = o[p]) !== null && f !== void 0 || (o[p] = o == null ? void 0 : o[u]);
      }
    });
  }
  var s = L(L({}, n), o);
  return Object.keys(s).forEach(function(a) {
    s[a] === t[a] && delete s[a];
  }), s;
}
var Qn = typeof CSSINJS_STATISTIC < "u", Lt = !0;
function At() {
  for (var e = arguments.length, t = new Array(e), n = 0; n < e; n++)
    t[n] = arguments[n];
  if (!Qn)
    return Object.assign.apply(Object, [{}].concat(t));
  Lt = !1;
  var r = {};
  return t.forEach(function(o) {
    if (K(o) === "object") {
      var i = Object.keys(o);
      i.forEach(function(s) {
        Object.defineProperty(r, s, {
          configurable: !0,
          enumerable: !0,
          get: function() {
            return o[s];
          }
        });
      });
    }
  }), Lt = !0, r;
}
var mn = {};
function mi() {
}
var hi = function(t) {
  var n, r = t, o = mi;
  return Qn && typeof Proxy < "u" && (n = /* @__PURE__ */ new Set(), r = new Proxy(t, {
    get: function(s, a) {
      if (Lt) {
        var c;
        (c = n) === null || c === void 0 || c.add(a);
      }
      return s[a];
    }
  }), o = function(s, a) {
    var c;
    mn[s] = {
      global: Array.from(n),
      component: L(L({}, (c = mn[s]) === null || c === void 0 ? void 0 : c.component), a)
    };
  }), {
    token: r,
    keys: n,
    flush: o
  };
};
function hn(e, t, n) {
  if (typeof n == "function") {
    var r;
    return n(At(t, (r = t[e]) !== null && r !== void 0 ? r : {}));
  }
  return n ?? {};
}
function gi(e) {
  return e === "js" ? {
    max: Math.max,
    min: Math.min
  } : {
    max: function() {
      for (var n = arguments.length, r = new Array(n), o = 0; o < n; o++)
        r[o] = arguments[o];
      return "max(".concat(r.map(function(i) {
        return zt(i);
      }).join(","), ")");
    },
    min: function() {
      for (var n = arguments.length, r = new Array(n), o = 0; o < n; o++)
        r[o] = arguments[o];
      return "min(".concat(r.map(function(i) {
        return zt(i);
      }).join(","), ")");
    }
  };
}
var vi = 1e3 * 60 * 10, bi = /* @__PURE__ */ function() {
  function e() {
    Ee(this, e), T(this, "map", /* @__PURE__ */ new Map()), T(this, "objectIDMap", /* @__PURE__ */ new WeakMap()), T(this, "nextID", 0), T(this, "lastAccessBeat", /* @__PURE__ */ new Map()), T(this, "accessBeat", 0);
  }
  return Ce(e, [{
    key: "set",
    value: function(n, r) {
      this.clear();
      var o = this.getCompositeKey(n);
      this.map.set(o, r), this.lastAccessBeat.set(o, Date.now());
    }
  }, {
    key: "get",
    value: function(n) {
      var r = this.getCompositeKey(n), o = this.map.get(r);
      return this.lastAccessBeat.set(r, Date.now()), this.accessBeat += 1, o;
    }
  }, {
    key: "getCompositeKey",
    value: function(n) {
      var r = this, o = n.map(function(i) {
        return i && K(i) === "object" ? "obj_".concat(r.getObjectID(i)) : "".concat(K(i), "_").concat(i);
      });
      return o.join("|");
    }
  }, {
    key: "getObjectID",
    value: function(n) {
      if (this.objectIDMap.has(n))
        return this.objectIDMap.get(n);
      var r = this.nextID;
      return this.objectIDMap.set(n, r), this.nextID += 1, r;
    }
  }, {
    key: "clear",
    value: function() {
      var n = this;
      if (this.accessBeat > 1e4) {
        var r = Date.now();
        this.lastAccessBeat.forEach(function(o, i) {
          r - o > vi && (n.map.delete(i), n.lastAccessBeat.delete(i));
        }), this.accessBeat = 0;
      }
    }
  }]), e;
}(), gn = new bi();
function yi(e, t) {
  return l.useMemo(function() {
    var n = gn.get(t);
    if (n)
      return n;
    var r = e();
    return gn.set(t, r), r;
  }, t);
}
var Si = function() {
  return {};
};
function wi(e) {
  var t = e.useCSP, n = t === void 0 ? Si : t, r = e.useToken, o = e.usePrefix, i = e.getResetStyles, s = e.getCommonStyle, a = e.getCompUnitless;
  function c(d, h, b, g) {
    var m = Array.isArray(d) ? d[0] : d;
    function C(w) {
      return "".concat(String(m)).concat(w.slice(0, 1).toUpperCase()).concat(w.slice(1));
    }
    var _ = (g == null ? void 0 : g.unitless) || {}, x = typeof a == "function" ? a(d) : {}, S = L(L({}, x), {}, T({}, C("zIndexPopup"), !0));
    Object.keys(_).forEach(function(w) {
      S[C(w)] = _[w];
    });
    var E = L(L({}, g), {}, {
      unitless: S,
      prefixToken: C
    }), v = p(d, h, b, E), y = u(m, b, E);
    return function(w) {
      var P = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : w, $ = v(w, P), k = Z($, 2), R = k[1], M = y(P), A = Z(M, 2), I = A[0], j = A[1];
      return [I, R, j];
    };
  }
  function u(d, h, b) {
    var g = b.unitless, m = b.injectStyle, C = m === void 0 ? !0 : m, _ = b.prefixToken, x = b.ignore, S = function(y) {
      var w = y.rootCls, P = y.cssVar, $ = P === void 0 ? {} : P, k = r(), R = k.realToken;
      return Rr({
        path: [d],
        prefix: $.prefix,
        key: $.key,
        unitless: g,
        ignore: x,
        token: R,
        scope: w
      }, function() {
        var M = hn(d, R, h), A = pn(d, R, M, {
          deprecatedTokens: b == null ? void 0 : b.deprecatedTokens
        });
        return Object.keys(M).forEach(function(I) {
          A[_(I)] = A[I], delete A[I];
        }), A;
      }), null;
    }, E = function(y) {
      var w = r(), P = w.cssVar;
      return [function($) {
        return C && P ? /* @__PURE__ */ l.createElement(l.Fragment, null, /* @__PURE__ */ l.createElement(S, {
          rootCls: y,
          cssVar: P,
          component: d
        }), $) : $;
      }, P == null ? void 0 : P.key];
    };
    return E;
  }
  function p(d, h, b) {
    var g = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, m = Array.isArray(d) ? d : [d, d], C = Z(m, 1), _ = C[0], x = m.join("-"), S = e.layer || {
      name: "antd"
    };
    return function(E) {
      var v = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : E, y = r(), w = y.theme, P = y.realToken, $ = y.hashId, k = y.token, R = y.cssVar, M = o(), A = M.rootPrefixCls, I = M.iconPrefixCls, j = n(), ee = R ? "css" : "js", Y = yi(function() {
        var W = /* @__PURE__ */ new Set();
        return R && Object.keys(g.unitless || {}).forEach(function(ne) {
          W.add(lt(ne, R.prefix)), W.add(lt(ne, dn(_, R.prefix)));
        }), pi(ee, W);
      }, [ee, _, R == null ? void 0 : R.prefix]), ce = gi(ee), B = ce.max, D = ce.min, N = {
        theme: w,
        token: k,
        hashId: $,
        nonce: function() {
          return j.nonce;
        },
        clientOnly: g.clientOnly,
        layer: S,
        // antd is always at top of styles
        order: g.order || -999
      };
      typeof i == "function" && Nt(L(L({}, N), {}, {
        clientOnly: !1,
        path: ["Shared", A]
      }), function() {
        return i(k, {
          prefix: {
            rootPrefixCls: A,
            iconPrefixCls: I
          },
          csp: j
        });
      });
      var X = Nt(L(L({}, N), {}, {
        path: [x, E, I]
      }), function() {
        if (g.injectStyle === !1)
          return [];
        var W = hi(k), ne = W.token, z = W.flush, V = hn(_, P, b), Q = ".".concat(E), H = pn(_, P, V, {
          deprecatedTokens: g.deprecatedTokens
        });
        R && V && K(V) === "object" && Object.keys(V).forEach(function(ae) {
          V[ae] = "var(".concat(lt(ae, dn(_, R.prefix)), ")");
        });
        var re = At(ne, {
          componentCls: Q,
          prefixCls: E,
          iconCls: ".".concat(I),
          antCls: ".".concat(A),
          calc: Y,
          // @ts-ignore
          max: B,
          // @ts-ignore
          min: D
        }, R ? V : H), se = h(re, {
          hashId: $,
          prefixCls: E,
          rootPrefixCls: A,
          iconPrefixCls: I
        });
        z(_, H);
        var U = typeof s == "function" ? s(re, E, v, g.resetFont) : null;
        return [g.resetStyle === !1 ? null : U, se];
      });
      return [X, $];
    };
  }
  function f(d, h, b) {
    var g = arguments.length > 3 && arguments[3] !== void 0 ? arguments[3] : {}, m = p(d, h, b, L({
      resetStyle: !1,
      // Sub Style should default after root one
      order: -998
    }, g)), C = function(x) {
      var S = x.prefixCls, E = x.rootCls, v = E === void 0 ? S : E;
      return m(S, v), null;
    };
    return C;
  }
  return {
    genStyleHooks: c,
    genSubStyleComponent: f,
    genComponentStyleHook: p
  };
}
const G = Math.round;
function ht(e, t) {
  const n = e.replace(/^[^(]*\((.*)/, "$1").replace(/\).*/, "").match(/\d*\.?\d+%?/g) || [], r = n.map((o) => parseFloat(o));
  for (let o = 0; o < 3; o += 1)
    r[o] = t(r[o] || 0, n[o] || "", o);
  return n[3] ? r[3] = n[3].includes("%") ? r[3] / 100 : r[3] : r[3] = 1, r;
}
const vn = (e, t, n) => n === 0 ? e : e / 100;
function _e(e, t) {
  const n = t || 255;
  return e > n ? n : e < 0 ? 0 : e;
}
class de {
  constructor(t) {
    T(this, "isValid", !0), T(this, "r", 0), T(this, "g", 0), T(this, "b", 0), T(this, "a", 1), T(this, "_h", void 0), T(this, "_s", void 0), T(this, "_l", void 0), T(this, "_v", void 0), T(this, "_max", void 0), T(this, "_min", void 0), T(this, "_brightness", void 0);
    function n(r) {
      return r[0] in t && r[1] in t && r[2] in t;
    }
    if (t) if (typeof t == "string") {
      let o = function(i) {
        return r.startsWith(i);
      };
      const r = t.trim();
      /^#?[A-F\d]{3,8}$/i.test(r) ? this.fromHexString(r) : o("rgb") ? this.fromRgbString(r) : o("hsl") ? this.fromHslString(r) : (o("hsv") || o("hsb")) && this.fromHsvString(r);
    } else if (t instanceof de)
      this.r = t.r, this.g = t.g, this.b = t.b, this.a = t.a, this._h = t._h, this._s = t._s, this._l = t._l, this._v = t._v;
    else if (n("rgb"))
      this.r = _e(t.r), this.g = _e(t.g), this.b = _e(t.b), this.a = typeof t.a == "number" ? _e(t.a, 1) : 1;
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
    const n = t(this.r), r = t(this.g), o = t(this.b);
    return 0.2126 * n + 0.7152 * r + 0.0722 * o;
  }
  getHue() {
    if (typeof this._h > "u") {
      const t = this.getMax() - this.getMin();
      t === 0 ? this._h = 0 : this._h = G(60 * (this.r === this.getMax() ? (this.g - this.b) / t + (this.g < this.b ? 6 : 0) : this.g === this.getMax() ? (this.b - this.r) / t + 2 : (this.r - this.g) / t + 4));
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
    const n = this.getHue(), r = this.getSaturation();
    let o = this.getLightness() - t / 100;
    return o < 0 && (o = 0), this._c({
      h: n,
      s: r,
      l: o,
      a: this.a
    });
  }
  lighten(t = 10) {
    const n = this.getHue(), r = this.getSaturation();
    let o = this.getLightness() + t / 100;
    return o > 1 && (o = 1), this._c({
      h: n,
      s: r,
      l: o,
      a: this.a
    });
  }
  /**
   * Mix the current color a given amount with another color, from 0 to 100.
   * 0 means no mixing (return current color).
   */
  mix(t, n = 50) {
    const r = this._c(t), o = n / 100, i = (a) => (r[a] - this[a]) * o + this[a], s = {
      r: G(i("r")),
      g: G(i("g")),
      b: G(i("b")),
      a: G(i("a") * 100) / 100
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
    const n = this._c(t), r = this.a + n.a * (1 - this.a), o = (i) => G((this[i] * this.a + n[i] * n.a * (1 - this.a)) / r);
    return this._c({
      r: o("r"),
      g: o("g"),
      b: o("b"),
      a: r
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
    const r = (this.g || 0).toString(16);
    t += r.length === 2 ? r : "0" + r;
    const o = (this.b || 0).toString(16);
    if (t += o.length === 2 ? o : "0" + o, typeof this.a == "number" && this.a >= 0 && this.a < 1) {
      const i = G(this.a * 255).toString(16);
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
    const t = this.getHue(), n = G(this.getSaturation() * 100), r = G(this.getLightness() * 100);
    return this.a !== 1 ? `hsla(${t},${n}%,${r}%,${this.a})` : `hsl(${t},${n}%,${r}%)`;
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
  _sc(t, n, r) {
    const o = this.clone();
    return o[t] = _e(n, r), o;
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
    function r(o, i) {
      return parseInt(n[o] + n[i || o], 16);
    }
    n.length < 6 ? (this.r = r(0), this.g = r(1), this.b = r(2), this.a = n[3] ? r(3) / 255 : 1) : (this.r = r(0, 1), this.g = r(2, 3), this.b = r(4, 5), this.a = n[6] ? r(6, 7) / 255 : 1);
  }
  fromHsl({
    h: t,
    s: n,
    l: r,
    a: o
  }) {
    if (this._h = t % 360, this._s = n, this._l = r, this.a = typeof o == "number" ? o : 1, n <= 0) {
      const d = G(r * 255);
      this.r = d, this.g = d, this.b = d;
    }
    let i = 0, s = 0, a = 0;
    const c = t / 60, u = (1 - Math.abs(2 * r - 1)) * n, p = u * (1 - Math.abs(c % 2 - 1));
    c >= 0 && c < 1 ? (i = u, s = p) : c >= 1 && c < 2 ? (i = p, s = u) : c >= 2 && c < 3 ? (s = u, a = p) : c >= 3 && c < 4 ? (s = p, a = u) : c >= 4 && c < 5 ? (i = p, a = u) : c >= 5 && c < 6 && (i = u, a = p);
    const f = r - u / 2;
    this.r = G((i + f) * 255), this.g = G((s + f) * 255), this.b = G((a + f) * 255);
  }
  fromHsv({
    h: t,
    s: n,
    v: r,
    a: o
  }) {
    this._h = t % 360, this._s = n, this._v = r, this.a = typeof o == "number" ? o : 1;
    const i = G(r * 255);
    if (this.r = i, this.g = i, this.b = i, n <= 0)
      return;
    const s = t / 60, a = Math.floor(s), c = s - a, u = G(r * (1 - n) * 255), p = G(r * (1 - n * c) * 255), f = G(r * (1 - n * (1 - c)) * 255);
    switch (a) {
      case 0:
        this.g = f, this.b = u;
        break;
      case 1:
        this.r = p, this.b = u;
        break;
      case 2:
        this.r = u, this.b = f;
        break;
      case 3:
        this.r = u, this.g = p;
        break;
      case 4:
        this.r = f, this.g = u;
        break;
      case 5:
      default:
        this.g = u, this.b = p;
        break;
    }
  }
  fromHsvString(t) {
    const n = ht(t, vn);
    this.fromHsv({
      h: n[0],
      s: n[1],
      v: n[2],
      a: n[3]
    });
  }
  fromHslString(t) {
    const n = ht(t, vn);
    this.fromHsl({
      h: n[0],
      s: n[1],
      l: n[2],
      a: n[3]
    });
  }
  fromRgbString(t) {
    const n = ht(t, (r, o) => (
      // Convert percentage to number. e.g. 50% -> 128
      o.includes("%") ? G(r / 100 * 255) : r
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
function gt(e) {
  return e >= 0 && e <= 255;
}
function $e(e, t) {
  const {
    r: n,
    g: r,
    b: o,
    a: i
  } = new de(e).toRgb();
  if (i < 1)
    return e;
  const {
    r: s,
    g: a,
    b: c
  } = new de(t).toRgb();
  for (let u = 0.01; u <= 1; u += 0.01) {
    const p = Math.round((n - s * (1 - u)) / u), f = Math.round((r - a * (1 - u)) / u), d = Math.round((o - c * (1 - u)) / u);
    if (gt(p) && gt(f) && gt(d))
      return new de({
        r: p,
        g: f,
        b: d,
        a: Math.round(u * 100) / 100
      }).toRgbString();
  }
  return new de({
    r: n,
    g: r,
    b: o,
    a: 1
  }).toRgbString();
}
var Ci = function(e, t) {
  var n = {};
  for (var r in e) Object.prototype.hasOwnProperty.call(e, r) && t.indexOf(r) < 0 && (n[r] = e[r]);
  if (e != null && typeof Object.getOwnPropertySymbols == "function") for (var o = 0, r = Object.getOwnPropertySymbols(e); o < r.length; o++)
    t.indexOf(r[o]) < 0 && Object.prototype.propertyIsEnumerable.call(e, r[o]) && (n[r[o]] = e[r[o]]);
  return n;
};
function _i(e) {
  const {
    override: t
  } = e, n = Ci(e, ["override"]), r = Object.assign({}, t);
  Object.keys(Ei).forEach((d) => {
    delete r[d];
  });
  const o = Object.assign(Object.assign({}, n), r), i = 480, s = 576, a = 768, c = 992, u = 1200, p = 1600;
  if (o.motion === !1) {
    const d = "0s";
    o.motionDurationFast = d, o.motionDurationMid = d, o.motionDurationSlow = d;
  }
  return Object.assign(Object.assign(Object.assign({}, o), {
    // ============== Background ============== //
    colorFillContent: o.colorFillSecondary,
    colorFillContentHover: o.colorFill,
    colorFillAlter: o.colorFillQuaternary,
    colorBgContainerDisabled: o.colorFillTertiary,
    // ============== Split ============== //
    colorBorderBg: o.colorBgContainer,
    colorSplit: $e(o.colorBorderSecondary, o.colorBgContainer),
    // ============== Text ============== //
    colorTextPlaceholder: o.colorTextQuaternary,
    colorTextDisabled: o.colorTextQuaternary,
    colorTextHeading: o.colorText,
    colorTextLabel: o.colorTextSecondary,
    colorTextDescription: o.colorTextTertiary,
    colorTextLightSolid: o.colorWhite,
    colorHighlight: o.colorError,
    colorBgTextHover: o.colorFillSecondary,
    colorBgTextActive: o.colorFill,
    colorIcon: o.colorTextTertiary,
    colorIconHover: o.colorText,
    colorErrorOutline: $e(o.colorErrorBg, o.colorBgContainer),
    colorWarningOutline: $e(o.colorWarningBg, o.colorBgContainer),
    // Font
    fontSizeIcon: o.fontSizeSM,
    // Line
    lineWidthFocus: o.lineWidth * 3,
    // Control
    lineWidth: o.lineWidth,
    controlOutlineWidth: o.lineWidth * 2,
    // Checkbox size and expand icon size
    controlInteractiveSize: o.controlHeight / 2,
    controlItemBgHover: o.colorFillTertiary,
    controlItemBgActive: o.colorPrimaryBg,
    controlItemBgActiveHover: o.colorPrimaryBgHover,
    controlItemBgActiveDisabled: o.colorFill,
    controlTmpOutline: o.colorFillQuaternary,
    controlOutline: $e(o.colorPrimaryBg, o.colorBgContainer),
    lineType: o.lineType,
    borderRadius: o.borderRadius,
    borderRadiusXS: o.borderRadiusXS,
    borderRadiusSM: o.borderRadiusSM,
    borderRadiusLG: o.borderRadiusLG,
    fontWeightStrong: 600,
    opacityLoading: 0.65,
    linkDecoration: "none",
    linkHoverDecoration: "none",
    linkFocusDecoration: "none",
    controlPaddingHorizontal: 12,
    controlPaddingHorizontalSM: 8,
    paddingXXS: o.sizeXXS,
    paddingXS: o.sizeXS,
    paddingSM: o.sizeSM,
    padding: o.size,
    paddingMD: o.sizeMD,
    paddingLG: o.sizeLG,
    paddingXL: o.sizeXL,
    paddingContentHorizontalLG: o.sizeLG,
    paddingContentVerticalLG: o.sizeMS,
    paddingContentHorizontal: o.sizeMS,
    paddingContentVertical: o.sizeSM,
    paddingContentHorizontalSM: o.size,
    paddingContentVerticalSM: o.sizeXS,
    marginXXS: o.sizeXXS,
    marginXS: o.sizeXS,
    marginSM: o.sizeSM,
    margin: o.size,
    marginMD: o.sizeMD,
    marginLG: o.sizeLG,
    marginXL: o.sizeXL,
    marginXXL: o.sizeXXL,
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
    screenMDMax: c - 1,
    screenLG: c,
    screenLGMin: c,
    screenLGMax: u - 1,
    screenXL: u,
    screenXLMin: u,
    screenXLMax: p - 1,
    screenXXL: p,
    screenXXLMin: p,
    boxShadowPopoverArrow: "2px 2px 5px rgba(0, 0, 0, 0.05)",
    boxShadowCard: `
      0 1px 2px -2px ${new de("rgba(0, 0, 0, 0.16)").toRgbString()},
      0 3px 6px 0 ${new de("rgba(0, 0, 0, 0.12)").toRgbString()},
      0 5px 12px 4px ${new de("rgba(0, 0, 0, 0.09)").toRgbString()}
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
  }), r);
}
const Li = {
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
}, Ri = Ir(He.defaultAlgorithm), Ii = {
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
}, Yn = (e, t, n) => {
  const r = n.getDerivativeToken(e), {
    override: o,
    ...i
  } = t;
  let s = {
    ...r,
    override: o
  };
  return s = _i(s), i && Object.entries(i).forEach(([a, c]) => {
    const {
      theme: u,
      ...p
    } = c;
    let f = p;
    u && (f = Yn({
      ...s,
      ...p
    }, {
      override: p
    }, u)), s[a] = f;
  }), s;
};
function Mi() {
  const {
    token: e,
    hashed: t,
    theme: n = Ri,
    override: r,
    cssVar: o
  } = l.useContext(He._internalContext), [i, s, a] = Mr(n, [He.defaultSeed, e], {
    salt: `${vo}-${t || ""}`,
    override: r,
    getComputedToken: Yn,
    cssVar: o && {
      prefix: o.prefix,
      key: o.key,
      unitless: Li,
      ignore: Ti,
      preserve: Ii
    }
  });
  return [n, a, t ? s : "", i, o];
}
const {
  genStyleHooks: Pi,
  genComponentStyleHook: rs,
  genSubStyleComponent: os
} = wi({
  usePrefix: () => {
    const {
      getPrefixCls: e,
      iconPrefixCls: t
    } = Ue();
    return {
      iconPrefixCls: t,
      rootPrefixCls: e()
    };
  },
  useToken: () => {
    const [e, t, n, r, o] = Mi();
    return {
      theme: e,
      realToken: t,
      hashId: n,
      token: r,
      cssVar: o
    };
  },
  useCSP: () => {
    const {
      csp: e
    } = Ue();
    return e ?? {};
  },
  layer: {
    name: "antdx",
    dependencies: ["antd"]
  }
}), Oi = (e) => {
  const {
    componentCls: t,
    calc: n
  } = e, r = `${t}-list-card`, o = n(e.fontSize).mul(e.lineHeight).mul(2).add(e.paddingSM).add(e.paddingSM).equal();
  return {
    [r]: {
      borderRadius: e.borderRadius,
      position: "relative",
      background: e.colorFillContent,
      borderWidth: e.lineWidth,
      borderStyle: "solid",
      borderColor: "transparent",
      flex: "none",
      // =============================== Desc ================================
      [`${r}-name,${r}-desc`]: {
        display: "flex",
        flexWrap: "nowrap",
        maxWidth: "100%"
      },
      [`${r}-ellipsis-prefix`]: {
        flex: "0 1 auto",
        minWidth: 0,
        overflow: "hidden",
        textOverflow: "ellipsis",
        whiteSpace: "nowrap"
      },
      [`${r}-ellipsis-suffix`]: {
        flex: "none"
      },
      // ============================= Overview ==============================
      "&-type-overview": {
        padding: n(e.paddingSM).sub(e.lineWidth).equal(),
        paddingInlineStart: n(e.padding).add(e.lineWidth).equal(),
        display: "flex",
        flexWrap: "nowrap",
        gap: e.paddingXS,
        alignItems: "flex-start",
        width: 236,
        // Icon
        [`${r}-icon`]: {
          fontSize: n(e.fontSizeLG).mul(2).equal(),
          lineHeight: 1,
          paddingTop: n(e.paddingXXS).mul(1.5).equal(),
          flex: "none"
        },
        // Content
        [`${r}-content`]: {
          flex: "auto",
          minWidth: 0,
          display: "flex",
          flexDirection: "column",
          alignItems: "stretch"
        },
        [`${r}-desc`]: {
          color: e.colorTextTertiary
        }
      },
      // ============================== Preview ==============================
      "&-type-preview": {
        width: o,
        height: o,
        lineHeight: 1,
        [`&:not(${r}-status-error)`]: {
          border: 0
        },
        // Img
        img: {
          width: "100%",
          height: "100%",
          verticalAlign: "top",
          objectFit: "cover",
          borderRadius: "inherit"
        },
        // Mask
        [`${r}-img-mask`]: {
          position: "absolute",
          inset: 0,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          background: `rgba(0, 0, 0, ${e.opacityLoading})`,
          borderRadius: "inherit"
        },
        // Error
        [`&${r}-status-error`]: {
          [`img, ${r}-img-mask`]: {
            borderRadius: n(e.borderRadius).sub(e.lineWidth).equal()
          },
          [`${r}-desc`]: {
            paddingInline: e.paddingXXS
          }
        },
        // Progress
        [`${r}-progress`]: {}
      },
      // ============================ Remove Icon ============================
      [`${r}-remove`]: {
        position: "absolute",
        top: 0,
        insetInlineEnd: 0,
        border: 0,
        padding: e.paddingXXS,
        background: "transparent",
        lineHeight: 1,
        transform: "translate(50%, -50%)",
        fontSize: e.fontSize,
        cursor: "pointer",
        opacity: e.opacityLoading,
        display: "none",
        "&:dir(rtl)": {
          transform: "translate(-50%, -50%)"
        },
        "&:hover": {
          opacity: 1
        },
        "&:active": {
          opacity: e.opacityLoading
        }
      },
      [`&:hover ${r}-remove`]: {
        display: "block"
      },
      // ============================== Status ===============================
      "&-status-error": {
        borderColor: e.colorError,
        [`${r}-desc`]: {
          color: e.colorError
        }
      },
      // ============================== Motion ===============================
      "&-motion": {
        transition: ["opacity", "width", "margin", "padding"].map((i) => `${i} ${e.motionDurationSlow}`).join(","),
        "&-appear-start": {
          width: 0,
          transition: "none"
        },
        "&-leave-active": {
          opacity: 0,
          width: 0,
          paddingInline: 0,
          borderInlineWidth: 0,
          marginInlineEnd: n(e.paddingSM).mul(-1).equal()
        }
      }
    }
  };
}, Tt = {
  "&, *": {
    boxSizing: "border-box"
  }
}, Fi = (e) => {
  const {
    componentCls: t,
    calc: n,
    antCls: r
  } = e, o = `${t}-drop-area`, i = `${t}-placeholder`;
  return {
    // ============================== Full Screen ==============================
    [o]: {
      position: "absolute",
      inset: 0,
      zIndex: e.zIndexPopupBase,
      ...Tt,
      "&-on-body": {
        position: "fixed",
        inset: 0
      },
      "&-hide-placement": {
        [`${i}-inner`]: {
          display: "none"
        }
      },
      [i]: {
        padding: 0
      }
    },
    "&": {
      // ============================= Placeholder =============================
      [i]: {
        height: "100%",
        borderRadius: e.borderRadius,
        borderWidth: e.lineWidthBold,
        borderStyle: "dashed",
        borderColor: "transparent",
        padding: e.padding,
        position: "relative",
        backdropFilter: "blur(10px)",
        background: e.colorBgPlaceholderHover,
        ...Tt,
        [`${r}-upload-wrapper ${r}-upload${r}-upload-btn`]: {
          padding: 0
        },
        [`&${i}-drag-in`]: {
          borderColor: e.colorPrimaryHover
        },
        [`&${i}-disabled`]: {
          opacity: 0.25,
          pointerEvents: "none"
        },
        [`${i}-inner`]: {
          gap: n(e.paddingXXS).div(2).equal()
        },
        [`${i}-icon`]: {
          fontSize: e.fontSizeHeading2,
          lineHeight: 1
        },
        [`${i}-title${i}-title`]: {
          margin: 0,
          fontSize: e.fontSize,
          lineHeight: e.lineHeight
        },
        [`${i}-description`]: {}
      }
    }
  };
}, Ai = (e) => {
  const {
    componentCls: t,
    calc: n
  } = e, r = `${t}-list`, o = n(e.fontSize).mul(e.lineHeight).mul(2).add(e.paddingSM).add(e.paddingSM).equal();
  return {
    [t]: {
      position: "relative",
      width: "100%",
      ...Tt,
      // =============================== File List ===============================
      [r]: {
        display: "flex",
        flexWrap: "wrap",
        gap: e.paddingSM,
        fontSize: e.fontSize,
        lineHeight: e.lineHeight,
        color: e.colorText,
        paddingBlock: e.paddingSM,
        paddingInline: e.padding,
        width: "100%",
        background: e.colorBgContainer,
        // Hide scrollbar
        scrollbarWidth: "none",
        "-ms-overflow-style": "none",
        "&::-webkit-scrollbar": {
          display: "none"
        },
        // Scroll
        "&-overflow-scrollX, &-overflow-scrollY": {
          "&:before, &:after": {
            content: '""',
            position: "absolute",
            opacity: 0,
            transition: `opacity ${e.motionDurationSlow}`,
            zIndex: 1
          }
        },
        "&-overflow-ping-start:before": {
          opacity: 1
        },
        "&-overflow-ping-end:after": {
          opacity: 1
        },
        "&-overflow-scrollX": {
          overflowX: "auto",
          overflowY: "hidden",
          flexWrap: "nowrap",
          "&:before, &:after": {
            insetBlock: 0,
            width: 8
          },
          "&:before": {
            insetInlineStart: 0,
            background: "linear-gradient(to right, rgba(0,0,0,0.06), rgba(0,0,0,0));"
          },
          "&:after": {
            insetInlineEnd: 0,
            background: "linear-gradient(to left, rgba(0,0,0,0.06), rgba(0,0,0,0));"
          },
          "&:dir(rtl)": {
            "&:before": {
              background: "linear-gradient(to left, rgba(0,0,0,0.06), rgba(0,0,0,0));"
            },
            "&:after": {
              background: "linear-gradient(to right, rgba(0,0,0,0.06), rgba(0,0,0,0));"
            }
          }
        },
        "&-overflow-scrollY": {
          overflowX: "hidden",
          overflowY: "auto",
          maxHeight: n(o).mul(3).equal(),
          "&:before, &:after": {
            insetInline: 0,
            height: 8
          },
          "&:before": {
            insetBlockStart: 0,
            background: "linear-gradient(to bottom, rgba(0,0,0,0.06), rgba(0,0,0,0));"
          },
          "&:after": {
            insetBlockEnd: 0,
            background: "linear-gradient(to top, rgba(0,0,0,0.06), rgba(0,0,0,0));"
          }
        },
        // ======================================================================
        // ==                              Upload                              ==
        // ======================================================================
        "&-upload-btn": {
          width: o,
          height: o,
          fontSize: e.fontSizeHeading2,
          color: "#999"
        },
        // ======================================================================
        // ==                             PrevNext                             ==
        // ======================================================================
        "&-prev-btn, &-next-btn": {
          position: "absolute",
          top: "50%",
          transform: "translateY(-50%)",
          boxShadow: e.boxShadowTertiary,
          opacity: 0,
          pointerEvents: "none"
        },
        "&-prev-btn": {
          left: {
            _skip_check_: !0,
            value: e.padding
          }
        },
        "&-next-btn": {
          right: {
            _skip_check_: !0,
            value: e.padding
          }
        },
        "&:dir(ltr)": {
          [`&${r}-overflow-ping-start ${r}-prev-btn`]: {
            opacity: 1,
            pointerEvents: "auto"
          },
          [`&${r}-overflow-ping-end ${r}-next-btn`]: {
            opacity: 1,
            pointerEvents: "auto"
          }
        },
        "&:dir(rtl)": {
          [`&${r}-overflow-ping-end ${r}-prev-btn`]: {
            opacity: 1,
            pointerEvents: "auto"
          },
          [`&${r}-overflow-ping-start ${r}-next-btn`]: {
            opacity: 1,
            pointerEvents: "auto"
          }
        }
      }
    }
  };
}, $i = (e) => {
  const {
    colorBgContainer: t
  } = e;
  return {
    colorBgPlaceholderHover: new de(t).setA(0.85).toRgbString()
  };
}, Jn = Pi("Attachments", (e) => {
  const t = At(e, {});
  return [Fi(t), Ai(t), Oi(t)];
}, $i), ki = (e) => e.indexOf("image/") === 0, ke = 200;
function ji(e) {
  return new Promise((t) => {
    if (!e || !e.type || !ki(e.type)) {
      t("");
      return;
    }
    const n = new Image();
    if (n.onload = () => {
      const {
        width: r,
        height: o
      } = n, i = r / o, s = i > 1 ? ke : ke * i, a = i > 1 ? ke / i : ke, c = document.createElement("canvas");
      c.width = s, c.height = a, c.style.cssText = `position: fixed; left: 0; top: 0; width: ${s}px; height: ${a}px; z-index: 9999; display: none;`, document.body.appendChild(c), c.getContext("2d").drawImage(n, 0, 0, s, a);
      const p = c.toDataURL();
      document.body.removeChild(c), window.URL.revokeObjectURL(n.src), t(p);
    }, n.crossOrigin = "anonymous", e.type.startsWith("image/svg+xml")) {
      const r = new FileReader();
      r.onload = () => {
        r.result && typeof r.result == "string" && (n.src = r.result);
      }, r.readAsDataURL(e);
    } else if (e.type.startsWith("image/gif")) {
      const r = new FileReader();
      r.onload = () => {
        r.result && t(r.result);
      }, r.readAsDataURL(e);
    } else
      n.src = window.URL.createObjectURL(e);
  });
}
function Di() {
  return /* @__PURE__ */ l.createElement("svg", {
    width: "1em",
    height: "1em",
    viewBox: "0 0 16 16",
    version: "1.1",
    xmlns: "http://www.w3.org/2000/svg",
    xmlnsXlink: "http://www.w3.org/1999/xlink"
  }, /* @__PURE__ */ l.createElement("title", null, "audio"), /* @__PURE__ */ l.createElement("g", {
    stroke: "none",
    "stroke-width": "1",
    fill: "none",
    "fill-rule": "evenodd"
  }, /* @__PURE__ */ l.createElement("path", {
    d: "M14.1178571,4.0125 C14.225,4.11964286 14.2857143,4.26428571 14.2857143,4.41607143 L14.2857143,15.4285714 C14.2857143,15.7446429 14.0303571,16 13.7142857,16 L2.28571429,16 C1.96964286,16 1.71428571,15.7446429 1.71428571,15.4285714 L1.71428571,0.571428571 C1.71428571,0.255357143 1.96964286,0 2.28571429,0 L9.86964286,0 C10.0214286,0 10.1678571,0.0607142857 10.275,0.167857143 L14.1178571,4.0125 Z M10.7315824,7.11216117 C10.7428131,7.15148751 10.7485063,7.19218979 10.7485063,7.23309113 L10.7485063,8.07742614 C10.7484199,8.27364959 10.6183424,8.44607275 10.4296853,8.50003683 L8.32984514,9.09986306 L8.32984514,11.7071803 C8.32986605,12.5367078 7.67249692,13.217028 6.84345686,13.2454634 L6.79068592,13.2463395 C6.12766108,13.2463395 5.53916361,12.8217001 5.33010655,12.1924966 C5.1210495,11.563293 5.33842118,10.8709227 5.86959669,10.4741173 C6.40077221,10.0773119 7.12636292,10.0652587 7.67042486,10.4442027 L7.67020842,7.74937024 L7.68449368,7.74937024 C7.72405122,7.59919041 7.83988806,7.48101083 7.98924584,7.4384546 L10.1880418,6.81004755 C10.42156,6.74340323 10.6648954,6.87865515 10.7315824,7.11216117 Z M9.60714286,1.31785714 L12.9678571,4.67857143 L9.60714286,4.67857143 L9.60714286,1.31785714 Z",
    fill: "currentColor"
  })));
}
function zi(e) {
  const {
    percent: t
  } = e, {
    token: n
  } = He.useToken();
  return /* @__PURE__ */ l.createElement(mr, {
    type: "circle",
    percent: t,
    size: n.fontSizeHeading2 * 2,
    strokeColor: "#FFF",
    trailColor: "rgba(255, 255, 255, 0.3)",
    format: (r) => /* @__PURE__ */ l.createElement("span", {
      style: {
        color: "#FFF"
      }
    }, (r || 0).toFixed(0), "%")
  });
}
function Ni() {
  return /* @__PURE__ */ l.createElement("svg", {
    width: "1em",
    height: "1em",
    viewBox: "0 0 16 16",
    version: "1.1",
    xmlns: "http://www.w3.org/2000/svg",
    xmlnsXlink: "http://www.w3.org/1999/xlink"
  }, /* @__PURE__ */ l.createElement("title", null, "video"), /* @__PURE__ */ l.createElement("g", {
    stroke: "none",
    "stroke-width": "1",
    fill: "none",
    "fill-rule": "evenodd"
  }, /* @__PURE__ */ l.createElement("path", {
    d: "M14.1178571,4.0125 C14.225,4.11964286 14.2857143,4.26428571 14.2857143,4.41607143 L14.2857143,15.4285714 C14.2857143,15.7446429 14.0303571,16 13.7142857,16 L2.28571429,16 C1.96964286,16 1.71428571,15.7446429 1.71428571,15.4285714 L1.71428571,0.571428571 C1.71428571,0.255357143 1.96964286,0 2.28571429,0 L9.86964286,0 C10.0214286,0 10.1678571,0.0607142857 10.275,0.167857143 L14.1178571,4.0125 Z M12.9678571,4.67857143 L9.60714286,1.31785714 L9.60714286,4.67857143 L12.9678571,4.67857143 Z M10.5379461,10.3101106 L6.68957555,13.0059749 C6.59910784,13.0693494 6.47439406,13.0473861 6.41101953,12.9569184 C6.3874624,12.9232903 6.37482581,12.8832269 6.37482581,12.8421686 L6.37482581,7.45043999 C6.37482581,7.33998304 6.46436886,7.25043999 6.57482581,7.25043999 C6.61588409,7.25043999 6.65594753,7.26307658 6.68957555,7.28663371 L10.5379461,9.98249803 C10.6284138,10.0458726 10.6503772,10.1705863 10.5870027,10.2610541 C10.5736331,10.2801392 10.5570312,10.2967411 10.5379461,10.3101106 Z",
    fill: "currentColor"
  })));
}
const vt = " ", Rt = "#8c8c8c", er = ["png", "jpg", "jpeg", "gif", "bmp", "webp", "svg"], Hi = [{
  icon: /* @__PURE__ */ l.createElement(br, null),
  color: "#22b35e",
  ext: ["xlsx", "xls"]
}, {
  icon: /* @__PURE__ */ l.createElement(yr, null),
  color: Rt,
  ext: er
}, {
  icon: /* @__PURE__ */ l.createElement(Sr, null),
  color: Rt,
  ext: ["md", "mdx"]
}, {
  icon: /* @__PURE__ */ l.createElement(wr, null),
  color: "#ff4d4f",
  ext: ["pdf"]
}, {
  icon: /* @__PURE__ */ l.createElement(xr, null),
  color: "#ff6e31",
  ext: ["ppt", "pptx"]
}, {
  icon: /* @__PURE__ */ l.createElement(Er, null),
  color: "#1677ff",
  ext: ["doc", "docx"]
}, {
  icon: /* @__PURE__ */ l.createElement(Cr, null),
  color: "#fab714",
  ext: ["zip", "rar", "7z", "tar", "gz"]
}, {
  icon: /* @__PURE__ */ l.createElement(Ni, null),
  color: "#ff4d4f",
  ext: ["mp4", "avi", "mov", "wmv", "flv", "mkv"]
}, {
  icon: /* @__PURE__ */ l.createElement(Di, null),
  color: "#8c8c8c",
  ext: ["mp3", "wav", "flac", "ape", "aac", "ogg"]
}];
function bn(e, t) {
  return t.some((n) => e.toLowerCase() === `.${n}`);
}
function Ui(e) {
  let t = e;
  const n = ["B", "KB", "MB", "GB", "TB", "PB", "EB"];
  let r = 0;
  for (; t >= 1024 && r < n.length - 1; )
    t /= 1024, r++;
  return `${t.toFixed(0)} ${n[r]}`;
}
function Bi(e, t) {
  const {
    prefixCls: n,
    item: r,
    onRemove: o,
    className: i,
    style: s
  } = e, a = l.useContext(Re), {
    disabled: c
  } = a || {}, {
    name: u,
    size: p,
    percent: f,
    status: d = "done",
    description: h
  } = r, {
    getPrefixCls: b
  } = Ue(), g = b("attachment", n), m = `${g}-list-card`, [C, _, x] = Jn(g), [S, E] = l.useMemo(() => {
    const I = u || "", j = I.match(/^(.*)\.[^.]+$/);
    return j ? [j[1], I.slice(j[1].length)] : [I, ""];
  }, [u]), v = l.useMemo(() => bn(E, er), [E]), y = l.useMemo(() => h || (d === "uploading" ? `${f || 0}%` : d === "error" ? r.response || vt : p ? Ui(p) : vt), [d, f]), [w, P] = l.useMemo(() => {
    for (const {
      ext: I,
      icon: j,
      color: ee
    } of Hi)
      if (bn(E, I))
        return [j, ee];
    return [/* @__PURE__ */ l.createElement(gr, {
      key: "defaultIcon"
    }), Rt];
  }, [E]), [$, k] = l.useState();
  l.useEffect(() => {
    if (r.originFileObj) {
      let I = !0;
      return ji(r.originFileObj).then((j) => {
        I && k(j);
      }), () => {
        I = !1;
      };
    }
    k(void 0);
  }, [r.originFileObj]);
  let R = null;
  const M = r.thumbUrl || r.url || $, A = v && (r.originFileObj || M);
  return A ? R = /* @__PURE__ */ l.createElement(l.Fragment, null, /* @__PURE__ */ l.createElement("img", {
    alt: "preview",
    src: M
  }), d !== "done" && /* @__PURE__ */ l.createElement("div", {
    className: `${m}-img-mask`
  }, d === "uploading" && f !== void 0 && /* @__PURE__ */ l.createElement(zi, {
    percent: f,
    prefixCls: m
  }), d === "error" && /* @__PURE__ */ l.createElement("div", {
    className: `${m}-desc`
  }, /* @__PURE__ */ l.createElement("div", {
    className: `${m}-ellipsis-prefix`
  }, y)))) : R = /* @__PURE__ */ l.createElement(l.Fragment, null, /* @__PURE__ */ l.createElement("div", {
    className: `${m}-icon`,
    style: {
      color: P
    }
  }, w), /* @__PURE__ */ l.createElement("div", {
    className: `${m}-content`
  }, /* @__PURE__ */ l.createElement("div", {
    className: `${m}-name`
  }, /* @__PURE__ */ l.createElement("div", {
    className: `${m}-ellipsis-prefix`
  }, S ?? vt), /* @__PURE__ */ l.createElement("div", {
    className: `${m}-ellipsis-suffix`
  }, E)), /* @__PURE__ */ l.createElement("div", {
    className: `${m}-desc`
  }, /* @__PURE__ */ l.createElement("div", {
    className: `${m}-ellipsis-prefix`
  }, y)))), C(/* @__PURE__ */ l.createElement("div", {
    className: oe(m, {
      [`${m}-status-${d}`]: d,
      [`${m}-type-preview`]: A,
      [`${m}-type-overview`]: !A
    }, i, _, x),
    style: s,
    ref: t
  }, R, !c && o && /* @__PURE__ */ l.createElement("button", {
    type: "button",
    className: `${m}-remove`,
    onClick: () => {
      o(r);
    }
  }, /* @__PURE__ */ l.createElement(vr, null))));
}
const tr = /* @__PURE__ */ l.forwardRef(Bi), yn = 1;
function Xi(e) {
  const {
    prefixCls: t,
    items: n,
    onRemove: r,
    overflow: o,
    upload: i,
    listClassName: s,
    listStyle: a,
    itemClassName: c,
    itemStyle: u
  } = e, p = `${t}-list`, f = l.useRef(null), [d, h] = l.useState(!1), {
    disabled: b
  } = l.useContext(Re);
  l.useEffect(() => (h(!0), () => {
    h(!1);
  }), []);
  const [g, m] = l.useState(!1), [C, _] = l.useState(!1), x = () => {
    const y = f.current;
    y && (o === "scrollX" ? (m(Math.abs(y.scrollLeft) >= yn), _(y.scrollWidth - y.clientWidth - Math.abs(y.scrollLeft) >= yn)) : o === "scrollY" && (m(y.scrollTop !== 0), _(y.scrollHeight - y.clientHeight !== y.scrollTop)));
  };
  l.useEffect(() => {
    x();
  }, [o]);
  const S = (y) => {
    const w = f.current;
    w && w.scrollTo({
      left: w.scrollLeft + y * w.clientWidth,
      behavior: "smooth"
    });
  }, E = () => {
    S(-1);
  }, v = () => {
    S(1);
  };
  return /* @__PURE__ */ l.createElement("div", {
    className: oe(p, {
      [`${p}-overflow-${e.overflow}`]: o,
      [`${p}-overflow-ping-start`]: g,
      [`${p}-overflow-ping-end`]: C
    }, s),
    ref: f,
    onScroll: x,
    style: a
  }, /* @__PURE__ */ l.createElement(li, {
    keys: n.map((y) => ({
      key: y.uid,
      item: y
    })),
    motionName: `${p}-card-motion`,
    component: !1,
    motionAppear: d,
    motionLeave: !0,
    motionEnter: !0
  }, ({
    key: y,
    item: w,
    className: P,
    style: $
  }) => /* @__PURE__ */ l.createElement(tr, {
    key: y,
    prefixCls: t,
    item: w,
    onRemove: r,
    className: oe(P, c),
    style: {
      ...$,
      ...u
    }
  })), !b && /* @__PURE__ */ l.createElement(Kn, {
    upload: i
  }, /* @__PURE__ */ l.createElement(st, {
    className: `${p}-upload-btn`,
    type: "dashed"
  }, /* @__PURE__ */ l.createElement(_r, {
    className: `${p}-upload-btn-icon`
  }))), o === "scrollX" && /* @__PURE__ */ l.createElement(l.Fragment, null, /* @__PURE__ */ l.createElement(st, {
    size: "small",
    shape: "circle",
    className: `${p}-prev-btn`,
    icon: /* @__PURE__ */ l.createElement(Lr, null),
    onClick: E
  }), /* @__PURE__ */ l.createElement(st, {
    size: "small",
    shape: "circle",
    className: `${p}-next-btn`,
    icon: /* @__PURE__ */ l.createElement(Tr, null),
    onClick: v
  })));
}
function Vi(e, t) {
  const {
    prefixCls: n,
    placeholder: r = {},
    upload: o,
    className: i,
    style: s
  } = e, a = `${n}-placeholder`, c = r || {}, {
    disabled: u
  } = l.useContext(Re), [p, f] = l.useState(!1), d = () => {
    f(!0);
  }, h = (m) => {
    m.currentTarget.contains(m.relatedTarget) || f(!1);
  }, b = () => {
    f(!1);
  }, g = /* @__PURE__ */ l.isValidElement(r) ? r : /* @__PURE__ */ l.createElement(hr, {
    align: "center",
    justify: "center",
    vertical: !0,
    className: `${a}-inner`
  }, /* @__PURE__ */ l.createElement(at.Text, {
    className: `${a}-icon`
  }, c.icon), /* @__PURE__ */ l.createElement(at.Title, {
    className: `${a}-title`,
    level: 5
  }, c.title), /* @__PURE__ */ l.createElement(at.Text, {
    className: `${a}-description`,
    type: "secondary"
  }, c.description));
  return /* @__PURE__ */ l.createElement("div", {
    className: oe(a, {
      [`${a}-drag-in`]: p,
      [`${a}-disabled`]: u
    }, i),
    onDragEnter: d,
    onDragLeave: h,
    onDrop: b,
    "aria-hidden": u,
    style: s
  }, /* @__PURE__ */ l.createElement(Cn.Dragger, Le({
    showUploadList: !1
  }, o, {
    ref: t,
    style: {
      padding: 0,
      border: 0,
      background: "transparent"
    }
  }), g));
}
const Wi = /* @__PURE__ */ l.forwardRef(Vi);
function Gi(e, t) {
  const {
    prefixCls: n,
    rootClassName: r,
    rootStyle: o,
    className: i,
    style: s,
    items: a,
    children: c,
    getDropContainer: u,
    placeholder: p,
    onChange: f,
    overflow: d,
    disabled: h,
    classNames: b = {},
    styles: g = {},
    ...m
  } = e, {
    getPrefixCls: C,
    direction: _
  } = Ue(), x = C("attachment", n), S = So("attachments"), {
    classNames: E,
    styles: v
  } = S, y = l.useRef(null), w = l.useRef(null);
  l.useImperativeHandle(t, () => ({
    nativeElement: y.current,
    upload: (B) => {
      var N, X;
      const D = (X = (N = w.current) == null ? void 0 : N.nativeElement) == null ? void 0 : X.querySelector('input[type="file"]');
      if (D) {
        const W = new DataTransfer();
        W.items.add(B), D.files = W.files, D.dispatchEvent(new Event("change", {
          bubbles: !0
        }));
      }
    }
  }));
  const [P, $, k] = Jn(x), R = oe($, k), [M, A] = Lo([], {
    value: a
  }), I = xe((B) => {
    A(B.fileList), f == null || f(B);
  }), j = {
    ...m,
    fileList: M,
    onChange: I
  }, ee = (B) => {
    const D = M.filter((N) => N.uid !== B.uid);
    I({
      file: B,
      fileList: D
    });
  };
  let Y;
  const ce = (B, D, N) => {
    const X = typeof p == "function" ? p(B) : p;
    return /* @__PURE__ */ l.createElement(Wi, {
      placeholder: X,
      upload: j,
      prefixCls: x,
      className: oe(E.placeholder, b.placeholder),
      style: {
        ...v.placeholder,
        ...g.placeholder,
        ...D == null ? void 0 : D.style
      },
      ref: N
    });
  };
  if (c)
    Y = /* @__PURE__ */ l.createElement(l.Fragment, null, /* @__PURE__ */ l.createElement(Kn, {
      upload: j,
      rootClassName: r,
      ref: w
    }, c), /* @__PURE__ */ l.createElement(tn, {
      getDropContainer: u,
      prefixCls: x,
      className: oe(R, r)
    }, ce("drop")));
  else {
    const B = M.length > 0;
    Y = /* @__PURE__ */ l.createElement("div", {
      className: oe(x, R, {
        [`${x}-rtl`]: _ === "rtl"
      }, i, r),
      style: {
        ...o,
        ...s
      },
      dir: _ || "ltr",
      ref: y
    }, /* @__PURE__ */ l.createElement(Xi, {
      prefixCls: x,
      items: M,
      onRemove: ee,
      overflow: d,
      upload: j,
      listClassName: oe(E.list, b.list),
      listStyle: {
        ...v.list,
        ...g.list,
        ...!B && {
          display: "none"
        }
      },
      itemClassName: oe(E.item, b.item),
      itemStyle: {
        ...v.item,
        ...g.item
      }
    }), ce("inline", B ? {
      style: {
        display: "none"
      }
    } : {}, w), /* @__PURE__ */ l.createElement(tn, {
      getDropContainer: u || (() => y.current),
      prefixCls: x,
      className: R
    }, ce("drop")));
  }
  return P(/* @__PURE__ */ l.createElement(Re.Provider, {
    value: {
      disabled: h
    }
  }, Y));
}
const nr = /* @__PURE__ */ l.forwardRef(Gi);
nr.FileCard = tr;
function Ki(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function qi(e, t = !1) {
  try {
    if (fr(e))
      return e;
    if (t && !Ki(e))
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
function te(e, t) {
  return xn(() => qi(e, t), [e, t]);
}
const Zi = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Qi(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const r = e[n];
    return t[n] = Yi(n, r), t;
  }, {}) : {};
}
function Yi(e, t) {
  return typeof t == "number" && !Zi.includes(e) ? t + "px" : t;
}
function It(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const o = l.Children.toArray(e._reactElement.props.children).map((i) => {
      if (l.isValidElement(i) && i.props.__slot__) {
        const {
          portals: s,
          clonedElement: a
        } = It(i.props.el);
        return l.cloneElement(i, {
          ...i.props,
          el: a,
          children: [...l.Children.toArray(i.props.children), ...s]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(Ne(l.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: s,
      type: a,
      useCapture: c
    }) => {
      n.addEventListener(a, s, c);
    });
  });
  const r = Array.from(e.childNodes);
  for (let o = 0; o < r.length; o++) {
    const i = r[o];
    if (i.nodeType === 1) {
      const {
        clonedElement: s,
        portals: a
      } = It(i);
      t.push(...a), n.appendChild(s);
    } else i.nodeType === 3 && n.appendChild(i.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function Ji(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const es = ar(({
  slot: e,
  clone: t,
  className: n,
  style: r,
  observeAttributes: o
}, i) => {
  const s = pe(), [a, c] = En([]), {
    forceClone: u
  } = dr(), p = u ? !0 : t;
  return we(() => {
    var b;
    if (!s.current || !e)
      return;
    let f = e;
    function d() {
      let g = f;
      if (f.tagName.toLowerCase() === "svelte-slot" && f.children.length === 1 && f.children[0] && (g = f.children[0], g.tagName.toLowerCase() === "react-portal-target" && g.children[0] && (g = g.children[0])), Ji(i, g), n && g.classList.add(...n.split(" ")), r) {
        const m = Qi(r);
        Object.keys(m).forEach((C) => {
          g.style[C] = m[C];
        });
      }
    }
    let h = null;
    if (p && window.MutationObserver) {
      let g = function() {
        var x, S, E;
        (x = s.current) != null && x.contains(f) && ((S = s.current) == null || S.removeChild(f));
        const {
          portals: C,
          clonedElement: _
        } = It(e);
        f = _, c(C), f.style.display = "contents", d(), (E = s.current) == null || E.appendChild(f);
      };
      g();
      const m = Br(() => {
        g(), h == null || h.disconnect(), h == null || h.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      h = new window.MutationObserver(m), h.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      f.style.display = "contents", d(), (b = s.current) == null || b.appendChild(f);
    return () => {
      var g, m;
      f.style.display = "", (g = s.current) != null && g.contains(f) && ((m = s.current) == null || m.removeChild(f)), h == null || h.disconnect();
    };
  }, [e, p, n, r, i, o]), l.createElement("react-child", {
    ref: s,
    style: {
      display: "contents"
    }
  }, ...a);
});
function Sn(e, t) {
  return e ? /* @__PURE__ */ ge.jsx(es, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function fe({
  key: e,
  slots: t,
  targets: n
}, r) {
  return t[e] ? (...o) => n ? n.map((i, s) => /* @__PURE__ */ ge.jsx(Dt, {
    params: o,
    forceClone: !0,
    children: Sn(i, {
      clone: !0,
      ...r
    })
  }, s)) : /* @__PURE__ */ ge.jsx(Dt, {
    params: o,
    forceClone: !0,
    children: Sn(t[e], {
      clone: !0,
      ...r
    })
  }) : void 0;
}
const ts = (e) => !!e.name;
function wn(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const is = go(({
  slots: e,
  upload: t,
  showUploadList: n,
  progress: r,
  beforeUpload: o,
  customRequest: i,
  previewFile: s,
  isImageUrl: a,
  itemRender: c,
  iconRender: u,
  data: p,
  onChange: f,
  onValueChange: d,
  onRemove: h,
  maxCount: b,
  items: g,
  setSlotParams: m,
  placeholder: C,
  getDropContainer: _,
  children: x,
  ...S
}) => {
  const E = e["showUploadList.downloadIcon"] || e["showUploadList.removeIcon"] || e["showUploadList.previewIcon"] || e["showUploadList.extra"] || typeof n == "object", v = wn(n), y = e["placeholder.title"] || e["placeholder.description"] || e["placeholder.icon"] || typeof C == "object", w = wn(C), P = te(v.showPreviewIcon), $ = te(v.showRemoveIcon), k = te(v.showDownloadIcon), R = te(o), M = te(i), A = te(r == null ? void 0 : r.format), I = te(s), j = te(a), ee = te(c), Y = te(u), ce = te(C, !0), B = te(_), D = te(p), N = pe(!1), [X, W] = En(g);
  we(() => {
    W(g);
  }, [g]);
  const ne = xn(() => (X == null ? void 0 : X.map((z) => ts(z) ? z : {
    ...z,
    name: z.orig_name || z.path,
    uid: z.uid || z.url || z.path,
    status: "done"
  })) || [], [X]);
  return /* @__PURE__ */ ge.jsxs(ge.Fragment, {
    children: [/* @__PURE__ */ ge.jsx("div", {
      style: {
        display: "none"
      },
      children: x
    }), /* @__PURE__ */ ge.jsx(nr, {
      ...S,
      getDropContainer: B,
      placeholder: e.placeholder ? fe({
        slots: e,
        setSlotParams: m,
        key: "placeholder"
      }) : y ? (...z) => {
        var V, Q, H;
        return {
          ...w,
          icon: e["placeholder.icon"] ? (V = fe({
            slots: e,
            setSlotParams: m,
            key: "placeholder.icon"
          })) == null ? void 0 : V(...z) : w.icon,
          title: e["placeholder.title"] ? (Q = fe({
            slots: e,
            setSlotParams: m,
            key: "placeholder.title"
          })) == null ? void 0 : Q(...z) : w.title,
          description: e["placeholder.description"] ? (H = fe({
            slots: e,
            setSlotParams: m,
            key: "placeholder.description"
          })) == null ? void 0 : H(...z) : w.description
        };
      } : ce || C,
      items: ne,
      data: D || p,
      previewFile: I,
      isImageUrl: j,
      maxCount: 1,
      itemRender: e.itemRender ? fe({
        slots: e,
        setSlotParams: m,
        key: "itemRender"
      }) : ee,
      iconRender: e.iconRender ? fe({
        slots: e,
        setSlotParams: m,
        key: "iconRender"
      }) : Y,
      onRemove: (z) => {
        if (N.current)
          return;
        h == null || h(z);
        const V = ne.findIndex((H) => H.uid === z.uid), Q = X.slice();
        Q.splice(V, 1), d == null || d(Q), f == null || f(Q.map((H) => H.path));
      },
      onChange: async (z) => {
        const V = z.file, Q = z.fileList;
        if (ne.find((H) => H.uid === V.uid)) {
          if (N.current)
            return;
          h == null || h(V);
          const H = ne.findIndex((se) => se.uid === V.uid), re = X.slice();
          re.splice(H, 1), d == null || d(re), f == null || f(re.map((se) => se.path));
        } else {
          if (R && !await R(V, Q) || N.current)
            return !1;
          N.current = !0;
          let H = Q;
          if (typeof b == "number") {
            const U = b - X.length;
            H = Q.slice(0, U < 0 ? 0 : U);
          } else if (b === 1)
            H = Q.slice(0, 1);
          else if (H.length === 0)
            return N.current = !1, !1;
          W((U) => [...b === 1 ? [] : U, ...H.map((ae) => ({
            ...ae,
            size: ae.size,
            uid: ae.uid,
            name: ae.name,
            status: "uploading"
          }))]);
          const re = (await t(H.map((U) => U.originFileObj))).filter((U) => U), se = b === 1 ? re : [...X.filter((U) => !re.some((ae) => ae.uid === U.uid)), ...re];
          N.current = !1, d == null || d(se), f == null || f(se.map((U) => U.path));
        }
      },
      customRequest: M || zr,
      progress: r && {
        ...r,
        format: A
      },
      showUploadList: E ? {
        ...v,
        showDownloadIcon: k || v.showDownloadIcon,
        showRemoveIcon: $ || v.showRemoveIcon,
        showPreviewIcon: P || v.showPreviewIcon,
        downloadIcon: e["showUploadList.downloadIcon"] ? fe({
          slots: e,
          setSlotParams: m,
          key: "showUploadList.downloadIcon"
        }) : v.downloadIcon,
        removeIcon: e["showUploadList.removeIcon"] ? fe({
          slots: e,
          setSlotParams: m,
          key: "showUploadList.removeIcon"
        }) : v.removeIcon,
        previewIcon: e["showUploadList.previewIcon"] ? fe({
          slots: e,
          setSlotParams: m,
          key: "showUploadList.previewIcon"
        }) : v.previewIcon,
        extra: e["showUploadList.extra"] ? fe({
          slots: e,
          setSlotParams: m,
          key: "showUploadList.extra"
        }) : v.extra
      } : n
    })]
  });
});
export {
  is as Attachments,
  is as default
};
